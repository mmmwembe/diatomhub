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

    image_path = "/content/drive/MyDrive/3 Mega LLC/Projects/Internal/Project_5_Algae_classification/2024-DiatomHub/Genera-LM/acanthoceras/acanthoceras_zachariasii_1_LM.jpg"

    st.image(image_path)

    if st.button("Delete Image"):
        if os.path.exists(image_path):
            os.remove(image_path)
            st.write("Image deleted successfully")
        else:
            st.write("Image does not exist")

if __name__ == '__main__':
    main()
