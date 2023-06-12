
# Custom Data Into Chat Bot Using LangChain And FAISS
This project provides a simplistic WebUI to users to upload any (.pdf) file and use it's data to Train our ChatBot.The file upload limit can range to anything below 200MB because of the StreamLit file restriction limit, which is used for the Development of the UI.

OPENAI's Embedding API is used for Vector Embedding of the data and then a Semantic Search Algorithm is performed to output the desired result.

Meta's Open source Semantic Seach Algoritm FAISS is being used to OutPut the desired Answer from the vector database.

Link for more details on how the semantic search is being performed - 
(https://github.com/facebookresearch/faiss)
## Get Started
To get started with the project -

1.) Clone the repository to your local system.

2.) Generate a new API key reference from OpenAI's website and paste it into the .env file present in the folder.

3.)Install the dependencies by -

```
pip install langchain,faiss-cpu,python-dotenv,Pypdf2,streamlit,openai
```
4.) Run the streamlit webUI by running the command -
```
streamlit run "{FILE PATH TO APP.PY FILE}"
```
## Screenshots
Interface When file is not loaded - 

![Screenshot (179)](https://github.com/shubhexists/MindWave/assets/110319892/5485d337-4ea6-456c-8859-3e0c298e4817)

Full Working Results -

![Screenshot (188)](https://github.com/shubhexists/MindWave/assets/110319892/1c542ed1-c6ac-40f4-a34f-19798f8e2515)

