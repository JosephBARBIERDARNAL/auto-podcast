import random
import string
import pandas as pd
import streamlit as st
from openai import OpenAI
from apikey import api_key

client = OpenAI(api_key=api_key)
model = 'gpt-3.5-turbo'

def generate_random_id(length=10):
    """Generate a random string of alphanumeric characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_response(prompt, context="", temperature=0.5, model=model):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": context}
        ],
        temperature=temperature
    )
    output = completion.choices[0].message.content
    return output

def simulate_conversation(persona1, persona2, topic, meta="", iterations=3):

    conversation_df = pd.DataFrame(columns=['Speaker', 'Message'])
    conversation_string = ""
    prompt = f"{persona1}\n{topic}\n{persona1.split(':')[0]}: "
    last_speaker = persona1.split(':')[0]

    for _ in range(iterations):
        response = get_response(prompt, context=meta)
        if last_speaker == persona1.split(':')[0]:
            current_speaker = persona2.split(':')[0]
        else:
            current_speaker = persona1.split(':')[0]

        new_row = pd.DataFrame({'Speaker': [current_speaker], 'Message': [response]})
        conversation_df = pd.concat([conversation_df, new_row], ignore_index=True)
        conversation_string += f"{current_speaker}: {response}\n"

        prompt += f"{current_speaker}: {response}\n"
        last_speaker = current_speaker
    
    return conversation_df, conversation_string
    
def remove_slash_n(text):
    return text.replace('\n', ' ')

def make_space(n):
    for _ in range(n):
        st.write('')


if __name__ == '__main__':
    pass