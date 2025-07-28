import streamlit as st
import requests
from PIL import Image
import io
import base64

st.set_page_config(page_title="AI Avatar Generator", page_icon="🧙")

st.title("🧙‍♂️ AI Avatar Generator")
st.markdown("Upload a photo and choose a style to generate a fantasy avatar using GenAI!")

uploaded_file = st.file_uploader("📸 Upload your photo", type=["jpg", "jpeg", "png"])

styles = ["Anime", "Pixar", "Cartoon", "Fantasy", "Cyberpunk"]
selected_style = st.selectbox("🎨 Choose Avatar Style", styles)

if uploaded_file and st.button("Generate Avatar"):
    st.info("⏳ Generating... This may take a few seconds.")

    # Convert image to base64
    img = Image.open(uploaded_file)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_b64 = base64.b64encode(buffered.getvalue()).decode()

    # Prepare prompt & API call (example uses Pollinations model via HuggingFace/Replicate/OpenRouter)
    prompt = f"A {selected_style.lower()} style avatar of the person in the uploaded photo"

    # Example call using a fake endpoint (replace this with real GenAI endpoint)
    api_url = "https://api.openrouter.ai/v1/fake-image-gen"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "image": img_b64,
        "prompt": prompt,
        "style": selected_style.lower()
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        avatar_url = result.get("generated_image_url")

        st.success("✨ Avatar Generated!")
        st.image(avatar_url, caption=f"{selected_style} Avatar", use_column_width=True)
    else:
        st.error("❌ Failed to generate avatar. Please check API key or try later.")
