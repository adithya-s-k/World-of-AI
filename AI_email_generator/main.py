import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect
    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.  
    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen
    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.
    Please start the email with a warm introduction. Add the introduction if you need to.
    
    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
  template=template,
  input_variables=["tone", "dialect", "email"],
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(client="Any", openai_api_key=openai_api_key)
    return llm

def validate_openai_api_key(api_key):
    """Validate the OpenAI API key format."""
    # Add your validation logic here
    if len(api_key) == 0:
        return False
    return True

def validate_email_input(email):
    """Validate the email input."""
    # Add your validation logic here
    if len(email.split(" ")) > 700:
        return False
    return True

def update_text_with_example():
    """Update the email input with an example."""
    st.session_state.email_input = "Sally I am starts work at yours Monday from Dave"

# Set up Streamlit page configuration
st.set_page_config(page_title="Email Generator", page_icon="email", layout="wide")

# Header
st.header("AI-powered Email Generator")

# About Section
st.write('Our AI email generator app is designed to help you save time and streamline your email communication. With our app, you can easily generate professional and effective emails in a matter of seconds, without having to spend hours crafting the perfect message. Our advanced algorithms analyze your input and generate highly personalized emails that are tailored to your specific needs. Our app is perfect for busy professionals who want to stay on top of their email correspondence and make a great impression on their clients and colleagues.')

# Features Section
st.header('Features')

col1, col2, col3 = st.columns(3)

with col1:
    st.write('**Personalized Emails**')
    st.write('Our app uses advanced algorithms to analyze your input and generate highly personalized emails that are tailored to your specific needs.')

with col2:
    st.write('**Time-Saving**')
    st.write('Our app helps you save time by generating professional and effective emails in a matter of seconds, without having to spend hours crafting the perfect message.')

with col3:
    st.write('**Easy-to-Use Interface**')
    st.write('Our app has an intuitive and user-friendly interface that makes it easy for anyone to use, even if they have no experience with email marketing or writing.')

with col1:
    st.write('**Customizable Templates**')
    st.write('Our app comes with a range of customizable templates that you can use to quickly generate emails for a variety of purposes, such as business proposals, job applications, and more.')

with col2:
    st.write('**Automated Follow-Ups**')
    st.write('Our app can automatically follow up on your emails, ensuring that you never miss an opportunity to connect with your clients or colleagues.')

with col3:
    st.write('**Insights and Analytics**')
    st.write('Our app provides you with insights and analytics about your email performance, including open rates, click-through rates, and more, so you can optimize your communication strategy over time.')

st.markdown("---")
st.header("Try it out!")

# Get the OpenAI API key
openai_api_key = st.text_input(label="Enter your OpenAI API Key", type="password", placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", key="openai_api_key")

# Validate the OpenAI API key
if not validate_openai_api_key(openai_api_key):
    st.warning('Please enter a valid OpenAI API key.')
    st.stop()

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox('Which tone would you like your email to have?', ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox('Which English Dialect would you like?', ('American', 'British'))

def get_text():
    input_text = st.text_area(label="Email Input", label_visibility='collapsed', placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

# Validate the email input
if not validate_email_input(email_input):
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

def generate_formatted_email(email_input, option_tone, option_dialect, openai_api_key):
    """Generate the formatted email using OpenAI API."""
    llm = load_LLM(openai_api_key=openai_api_key)
    prompt_final = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    formatted_email = llm(prompt_final)
    return formatted_email

def display_formatted_email(formatted_email):
    """Display the formatted email."""
    st.markdown(formatted_email)

# See an example button
st.button("*See An Example*", type='secondary', help="Click to see an example of the email you will be converting.", on_click=update_text_with_example)

st.markdown("### Your Converted Email:")

if email_input:
    formatted_email = generate_formatted_email(email_input, option_tone, option_dialect, openai_api_key)
    display_formatted_email(formatted_email)

st.markdown("---")
