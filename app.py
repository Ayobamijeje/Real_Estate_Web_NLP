import sys
import streamlit as st
from Housing import crawl_website


website_url = "https://hata.ng/lagos/houses-apartments-for-rent?price_max=2000000&price_min=400000"
app = crawl_website(website_url)



st.title(" :red[Lagos Housing Chatbot]")
st.write("#### Ask me about housing options in Lagos! 🏙️")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("How can I assist you with housing in Lagos?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    answer = app.query(prompt)

    if isinstance(answer, str):
        if "Answer:" in answer:
            response = answer.split("Answer:")[-1].strip()
        else:
            response = answer
    else:
        response = "I couldn't find a suitable answer for that."


    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})









