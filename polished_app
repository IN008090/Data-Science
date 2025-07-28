import streamlit as st
import requests

# Page config must be at the top
st.set_page_config(page_title="GenAI Chat App", page_icon="🤖")

# Sidebar
st.sidebar.title("🔧 Settings")
st.sidebar.markdown("""
- Enter your prompt in the main area  
- Powered by **OpenRouter API**  
- Enjoy chatting with your custom AI!
""")

# Main title
st.markdown("<h1 style='text-align: center;'>🤖 Your Personal GenAI Assistant</h1>", unsafe_allow_html=True)

# User input
user_input = st.text_area("🧠 Type your question below:")

# Submit button
if st.button("🚀 Generate Response"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            # Replace this with actual OpenRouter API call
            # Example: response = call_openrouter_api(user_input)
            response = "Your generated response here"
            st.success("Done!")
            st.markdown(f"**🤖 AI:** {response}")
