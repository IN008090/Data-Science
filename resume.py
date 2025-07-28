import streamlit as st
import requests

# Set page settings
st.set_page_config(page_title="🧠 AI Resume Builder", page_icon="📄")
st.title("📄 AI Resume & Cover Letter Generator")

# Sidebar for API Key and instructions
st.sidebar.title("🔧 Settings")
api_key = st.sidebar.text_input("Enter your OpenRouter API Key", type="password")
st.sidebar.markdown("""
This app uses **OpenRouter's free API** to generate a personalized resume and cover letter using GenAI.

💡 Use a model like `mistralai/mistral-7b-instruct` (free).
""")

# Collect user input
st.markdown("### 🧠 Tell Me About Yourself")
name = st.text_input("Full Name")
job_title = st.text_input("Job Title You Want")
experience = st.text_area("Your Experience Summary")
skills = st.text_input("List Your Skills (comma separated)")
education = st.text_input("Your Education")

# Generate resume button
if st.button("🚀 Generate Resume + Cover Letter"):
    if not api_key:
        st.error("❌ Please enter your API key in the sidebar.")
    elif not all([name, job_title, experience, skills, education]):
        st.warning("⚠️ Please fill all the fields.")
    else:
        with st.spinner("Thinking..."):
            # Prepare the prompt
            prompt = f"""
Generate a professional resume and cover letter for the following user:
Name: {name}
Target Job Title: {job_title}
Experience Summary: {experience}
Skills: {skills}
Education: {education}

Format: First provide the Resume, then the Cover Letter. Keep it clean and ATS-friendly.
"""

            # OpenRouter API call
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "mistralai/mistral-7b-instruct",
                "messages": [{"role": "user", "content": prompt}]
            }

            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
                res_json = response.json()

                # Check and display the result
                if "choices" in res_json:
                    reply = res_json["choices"][0]["message"]["content"]
                    st.success("✅ Done!")
                    st.markdown("### 📄 Generated Resume & Cover Letter")
                    st.markdown(reply)
                else:
                    st.error("❌ Failed to get response from OpenRouter API.")
                    st.json(res_json)  # helpful for debugging

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
