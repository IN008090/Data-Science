import streamlit as st
import requests

# Streamlit Page Config
st.set_page_config(page_title="Free GenAI via OpenRouter", layout="centered")
st.title("💬 Ask AI for Free (OpenRouter API)")

# Input API Key and Prompt
api_key = st.text_input("🔑 Enter your OpenRouter API Key", type="password")
prompt = st.text_area("💡 Your prompt", height=200)

# Generate Button
if st.button("🚀 Generate"):
    if api_key and prompt:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://your-username.streamlit.app",  # REQUIRED
            "X-Title": "FreeAIChatApp"
        }

        data = {
            "model": "mistralai/mistral-7b-instruct",  # or try gpt-3.5, meta-llama models
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                result = response.json()
                message = result['choices'][0]['message']['content']
                st.write("### 🤖 AI Response:")
                st.success(message)
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Exception: {e}")
    else:
        st.warning("Please enter both API key and prompt.")
