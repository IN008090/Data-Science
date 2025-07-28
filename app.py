import openai
import streamlit as st

st.set_page_config(page_title="Simple GenAI App", layout="centered")
st.title("💬 Ask AI Anything")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
prompt = st.text_area("Your prompt", height=200)

if api_key:
    openai.api_key = api_key

if st.button("Generate"):
    if api_key and prompt:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.write("### 🤖 AI Response:")
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please provide both API key and prompt.")
