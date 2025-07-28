import openai
import streamlit as st

st.set_page_config(page_title="Simple GenAI App", layout="centered")
st.title("💬 Ask AI Anything (via OpenRouter)")

# Input API key
user_api_key = st.text_input("Enter your OpenRouter API Key", type="password")

# Set OpenRouter base
openai.api_base = "https://openrouter.ai/api/v1"

# Prompt input
prompt = st.text_area("Your prompt", height=200)

if st.button("Generate"):
    if user_api_key and prompt:
        try:
            openai.api_key = user_api_key
            # Manual header injection
            response = openai.ChatCompletion.create(
                model="mistralai/mistral-7b-instruct",  # or other OpenRouter-supported models
                messages=[{"role": "user", "content": prompt}],
                headers={"Authorization": f"Bearer {user_api_key}"}
            )
            st.write("### 🤖 AI Response:")
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please provide both API key and prompt.")
