```markdown
# PDF Summarization and Text Categorization App

This is a Flask web application that allows users to upload PDF documents, extract the text content from them, summarize the text, and perform text categorization on the document. The application makes use of the Hugging Face Transformers library for summarization and text classification.

## Installation

1. Clone the repository:

   ```shell
   git clone [https://github.com/your-username/pdf-summarization.git](https://github.com/nayan-khemka/World-of-AI.git)
   ```

2. Navigate to the project directory:

   ```shell
   cd pdf-summarization
   ```

3. Create a virtual environment:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

5. Install the required packages:

   ```shell
   pip install -r requirements.txt
   ```

6. Run the application:

   ```shell
   python app.py
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000).

## Usage

1. Upload a PDF document by clicking on the "Choose File" button.

2. Click on the "Summarize" button to extract the text content, generate a summary, and perform text categorization on the document.

3. The application will display the summary and the category of the document.

## Customization

- If you want to change the design or layout of the application, you can modify the HTML templates in the `templates` directory.

- To use a different text classification model or modify the summarization parameters, you can update the code in `app.py` accordingly.

## License

This project is licensed under the [MIT License](LICENSE).
