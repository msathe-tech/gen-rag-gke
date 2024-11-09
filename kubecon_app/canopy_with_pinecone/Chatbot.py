import streamlit as st
import requests
import os

# Set up page configuration
st.set_page_config(page_title="Let's play with Canopy and PineCone", page_icon="💬")

# Hide Streamlit's default styles
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .css-1lsmgbg.egzxvld0 {visibility: hidden;} /* Hide the "Settings" button */
    .stAppDeployButton {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title of the app
st.title("💬 Chatbot Demo on Canopy and PineCone")

# Initialize the messages in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Radio buttons for API selection
option = st.radio("Choose an option:", ("Option A - for Canopy with PineCone", "Option B - Only OpenAI, no Pinecone"))

# Set CUSTOM_API_URL based on selection
if option == "Option A - for Canopy with PineCone":
    custom_api_url = os.getenv('CUSTOM_API_URL')  # Assuming you set this in your environment variables
else:  # Option B
    custom_api_url = os.getenv('CUSTOM_API_URL_OPB')  # Assuming this is your second API URL

# Check if the custom API URL is set
if not custom_api_url:
    st.info("The API URL is not set. Please set the CUSTOM_API_URL or CUSTOM_API_URL_OPB environment variable to continue.")
    st.stop()

# User input for chat
if prompt := st.chat_input():
    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Make a POST request to the custom LLM API
    try:
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": st.session_state.messages
        }
        response = requests.post(custom_api_url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            response_data = response.json()
            msg = response_data['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
