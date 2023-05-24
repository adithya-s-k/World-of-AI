import os
import random
from datetime import datetime, timedelta

import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

example_destinations = ['Kolkata', 'Mumbai', 'New Delhi', 'Chennai', 'Bangalore', 'Hyderabad', 'Lucknow', 'Jaipur', 'Ahmedabad', 'Pune']
random_destination = random.choice(example_destinations)

now_date = datetime.now()

now_date = now_date.replace(minute=now_date.minute // 15 * 15, second=0, microsecond=0)

now_time = now_date.time()
now_date = now_date.date() + timedelta(days=1)

def generate_prompt(destination, arrival_to, arrival_date, arrival_time, departure_from, departure_date, departure_time, additional_information, **kwargs):
    return f'''
Prepare trip schedule for {destination}, based on the following information:

* Arrival To: {arrival_to}
* Arrival Date: {arrival_date}
* Arrival Time: {arrival_time}

* Departure From: {departure_from}
* Departure Date: {departure_date}
* Departure Time: {departure_time}

* Additional Notes: {additional_information}
'''.strip()

def submit():
    try:
        with st.spinner("Let's see how can we best plan your trip..."):
            prompt = generate_prompt(**st.session_state)

            output = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                temperature=0.45,
                top_p=1,
                frequency_penalty=2,
                presence_penalty=0,
                max_tokens=2000
            )

            st.session_state['output'] = output['choices'][0]['text']
    except:
        st.error('Oops! Something went wrong on our side :) Please try again after some time!')

if 'output' not in st.session_state:
    st.session_state['output'] = '  '

st.set_page_config(page_title="Your AI based personal Tour Guide", page_icon="✈️")
st.title('AI Tour Guide')
st.subheader('Let us plan your trip!')

with st.form(key='trip_form'):
    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader('Destination')

        origin = st.text_input('Destination', value=random_destination, key='destination')

    with c2:
        st.subheader('Arrival')

        st.selectbox('Arrival To', ('Airport', 'Train Station', 'Bus Station', 'Other'), key='arrival_to')
        st.date_input('Arrival Date', value=now_date, key='arrival_date')
        st.time_input('Arrival Time', value=now_time, key='arrival_time')

    with c3:
        st.subheader('Departure')

        st.selectbox('Departure From', ('Airport', 'Train Station', 'Bus Station', 'Other'), key='departure_from')
        st.date_input('Departure Date', value=now_date + timedelta(days=1), key='departure_date')
        st.time_input('Departure Time', value=now_time, key='departure_time')

    st.text_area('Additional Information', height=200, value='I want to visit as many places as possible! (respect time)', key='additional_information')
    st.form_submit_button('Submit', on_click=submit)


if st.session_state.output != '  ':
    st.subheader('Tour Schedule')
    st.success(st.session_state.output)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer:before {content: '</> Developed by Debayudh Mitra | '}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)