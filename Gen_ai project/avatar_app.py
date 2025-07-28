import streamlit as st
import requests

# Set Streamlit page config
st.set_page_config(page_title="AI Avatar Generator", page_icon="🧙‍♂️")

# Title
st.title("🧙‍♂️ AI Avatar Generator")

# Sidebar for API key and instructions
st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("🔑 Enter your OpenRouter API Key", type="password")
st.sidebar.markdown("""
- Upload your image below (JPG/PNG).
- Select your style (Anime, Pixar, Cartoon, etc).
- Click 'Generate Avatar'!
""")

# Upload image
uploaded_file = st.file_uploader("📤 Upload your photo", type=["jpg", "jpeg", "png"])
style = st.selectbox("🎨 Choose avatar style", ["Anime", "Pixar", "Cartoon", "Fantasy"])

# Button to trigger generation
if st.button("🎨 Generate Avatar"):
    if not uploaded_file:
        st.warning("Please upload a photo first.")
    elif not api_key:
        st.warning("Please enter your OpenRouter API key in the sidebar.")
    else:
        # Simulated API call (replace with actual API call)
        with st.spinner("🧠 Generating your avatar..."):
            # You would call OpenRouter or any GenAI image API here
            # This is just a placeholder
            st.success("✅ Avatar generated!")
            st.image(uploaded_file, caption=f"{style} Avatar (Simulated)", use_column_width=True)
