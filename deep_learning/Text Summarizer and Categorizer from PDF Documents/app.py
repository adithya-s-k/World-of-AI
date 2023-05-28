from flask import Flask, render_template, request, redirect, url_for
import requests
from PyPDF2 import PdfReader

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
SUMMARY_LIMIT = 500

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return render_template("index.html", error="No file uploaded.")

        file = request.files["file"]

        # Check if the file is a PDF
        if file.filename.endswith(".pdf"):
            # Read the PDF content
            try:
                pdf = PdfReader(file)
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                
                text=text.replace(" ","").replace("\n"," ")
                # Summarize the document using Hugging Face API
                summary = summarize_with_api(text)

                # Truncate the summary to the desired limit
                # summary = truncate_summary(summary, SUMMARY_LIMIT)

                # Redirect to the summary page
                return redirect(url_for("display_summary", summary=summary))

            except PdfReader.PdfReadError:
                return render_template("index.html", error="Failed to read PDF.")

        else:
            return render_template("index.html", error="Please upload a PDF file.")

    return render_template("index.html")

@app.route("/summary")
def display_summary():
    summary = request.args.get("summary")
    return render_template("summary.html", summary=summary)

def summarize_with_api(text):
    # Prepare the data for the API request
    data = {
        "inputs": text,
        "parameters": {"max_length": 500, "min_length": 500, "num_beams": 4}
    }

    # Make the API request
    response = requests.post(API_URL, json=data)

    # Extract the summary from the API response
    response_json = response.json()[0]
    print(response_json)
    print(response.json())
    if "summary_text" in response_json:
        summary = response_json['summary_text']
        print(summary)
    else:
        summary = "Summary not available"

    return summary

def truncate_summary(summary, limit):
    if len(summary) > limit:
        summary = summary[:limit].rsplit(' ', 1)[0] + '...'
    return summary

if __name__ == "__main__":
    app.run(debug=True)
