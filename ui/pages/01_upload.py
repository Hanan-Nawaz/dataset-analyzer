import streamlit as st
from src.load_data import load_data

st.set_page_config(page_title="Upload Dataset",layout="wide")

st.subheader("Upload Dataset")
st.markdown("---")

file = st.file_uploader("Please select file", type=["csv", "xlsx"])
if file:
    df = load_data(file)
    st.success("Dataset file uploaded successfully!")
    st.session_state["df"] = df
else:
    st.warning("Please Upload the file")