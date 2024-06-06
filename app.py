import streamlit as st
from utils import *

context_cleaning = """
This discussion is not well formated. Clean it with proper format with name: message and new line for each message.
"""

description_podcast = """
You're in the podcast named "Auto podcast". This podcast is a discussion between two people about a topic.
The people don't know each other and they are discussing the topic for the first time together.
They are trying to have a natural conversation about the topic.
They start by saying hello, introducing themselves, and then they start discussing the topic.
The conversation is quite long and they discuss the topic in depth.
They question each other, ask for opinions, and give their own opinions.
Here starts the conversation.
"""


st.title('Auto podcast')
make_space(3)

col1, col2 = st.columns(2)
with col1:
   name1 = st.text_input('Name of the first person', key=1)
   persona1_description = st.text_area('Describe the first person', key=2)
   persona1 = f"{name1}: {persona1_description}"
with col2:
   name2 = st.text_input('Name of the second person', key=3)
   persona2_description = st.text_area('Describe the first person', key=4)
   persona2 = f"{name2}: {persona2_description}"
topic = st.text_area("Choose a topic", key=5)

if st.toggle('Generate random conversation'):
   df, conv = simulate_conversation(persona1, persona2, topic, meta=description_podcast, iterations=10)
   df['Message'] = df['Message'].apply(remove_slash_n)
   st.dataframe(df)
   make_space(3)
   cleaned_conv = get_response(conv, context=context_cleaning)
   st.markdown(cleaned_conv)