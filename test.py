import os
import streamlit as st
from utils import *
def main():
    st.set_page_config(page_title='PDF Summarizer')
    st.title('PDF Summarizer app')
    st.write("Summarize your PDF file in just a few seconds")
    st.divider()

    pdf = st.file_uploader('Upload your PDF file', type='pdf')

    submit=st.button('Generate Summary')

    api_key = os.environ.get("OPENAI_API_KEY")

if __name__ == '__main__':
    main()
