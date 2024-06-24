import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URL from the environment variables
db_url = os.getenv("DB_URL")

def main():
    st.title('Hello, World!')
    st.write("This is a simple Streamlit app deployed on Heroku.")
    # st.write(f"DB URL: {db_url}")  # For demonstration purposes only. Avoid printing sensitive information in real apps.

if __name__ == '__main__':
    main()

# import streamlit as st

# def main():
#     st.title('Diatom Hub')
#     st.write("This is a simple Streamlit app deployed on Heroku.")

# if __name__ == '__main__':
#     main()
