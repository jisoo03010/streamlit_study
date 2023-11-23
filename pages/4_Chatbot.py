import numpy as np
import pandas as pd
import requests
import streamlit as st
import streamlit.components.v1 as components
from st_aggrid import AgGrid, JsCode
from streamlit_chat import message

js_code = JsCode("""
function(params) {
    if (params.value > 0) {
        return {backgroundColor: 'green'}
    } else {
        return {backgroundColor: 'red'}
    }
}
""")
df = pd.DataFrame(
    np.random.randint(-100, 100, size=(100, 10)),
    columns=list('ABCDEFGHIJ'))
 
AgGrid(df)


API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
 
st.header("🤖Yunwoong's BlenderBot (Demo)")
 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
 
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    output = query({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },
        "parameters": {"repetition_penalty": 1.33},
    })
 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))