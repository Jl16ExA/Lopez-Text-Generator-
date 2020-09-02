# Example directly sending a text string:
import streamlit as st
import requests
import json
import os


st.title("""Lopez completa tu texto""")

user_input = st.text_area("Escribe tu texto aqui", '')

if st.button('Click'):
    r = requests.post(
        "https://api.inferkit.com/v1/models/standard/generate",

        json={



            "length": 500,
            "prompt": {
                "text": 'bin'
            },
        },
        headers={"Authorization": "Bearer 22d14de9-ddf7-4f1e-bf29-9973a205564f", }


    )

    x = r.json()
    y = x['data']

    stream = os.popen(y['text'])
    output = stream.read()
    print(y['text'])
    st.write(y['text'])
