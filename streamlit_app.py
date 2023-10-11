import streamlit as st
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set your OpenAI API key
openai.api_key = "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"

# Set your Google Sheets credentials file (JSON file you downloaded)
GOOGLE_SHEETS_CREDENTIALS = "your-credentials.json"

# Initialize the Google Sheets client
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEETS_CREDENTIALS, scope)
gc = gspread.authorize(credentials)

# Open a Google Sheet by its title
sheet = gc.open("Your Google Sheet Title").sheet1

# Streamlit UI
st.title("Chat with GPT-3.5")

# Input text box for user queries
user_input = st.text_area("Ask a question:")

if st.button("Get Answer"):
    # Make a request to GPT-3 for generating a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=50  # You can adjust this based on your needs
    )

    answer = response.choices[0].text.strip()

    # Display the response
    st.write("GPT-3's response:", answer)

# Display the Google Sheet data
st.write("Google Sheet Data")
data = sheet.get_all_values()
st.table(data)
