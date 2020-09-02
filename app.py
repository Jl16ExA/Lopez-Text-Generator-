# Example directly sending a text string:
import streamlit as st
import requests
import json


st.title("""Lopez completa tu texto""")

user_input = st.text_area("Escribe tu texto aqui", 'Daniel es Gay')

if st.button('Click'):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': user_input,
        },
        headers={'api-key': 'ef130802-1c85-417b-895c-d1f92982e595'}
    )
    x = r.json()
    print(x['output'])
    st.write(x['output'])
