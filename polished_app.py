import streamlit as st
import requests

# Set up Streamlit UI
st.set_page_config(page_title="GenAI Chat App", page_icon="🤖")
st.title("🤖 Your Personal GenAI Assistant")

st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("Enter your OpenRouter API Key", type="password")

st.sidebar.markdown("""
- Enter your prompt in the main area  
- Powered by **OpenRouter API**  
""")

# Main input
prompt = st.text_area("🧠 Type your question below:")

if st.button("🚀 Generate Response"):
    if not api_key:
        st.warning("🔑 Please enter your OpenRouter API Key in the sidebar.")
    elif not prompt.strip():
        st.warning("✍️ Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            # Make request to OpenRouter API
            try:
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "mistralai/mistral-7b-instruct",  # or any other available model
                    "messages": [{"role": "user", "content": prompt}]
                }

                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                reply = response.json()["choices"][0]["message"]["content"]

                st.success("Done!")
                st.markdown(f"**🤖 AI:** {reply}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
