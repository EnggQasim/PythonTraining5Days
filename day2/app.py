import streamlit as st
import pandas as pd

@st.cache
def load_metadata():
    DATA_URL = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz"
    return pd.read_csv(DATA_URL, nrows=1000)

@st.cache
def create_summary(metadata, summary_type):
    one_hot_encoded = pd.get_dummies(metadata[["frame", "label"]], columns=["label"])
    return getattr(one_hot_encoded.groupby(["frame"]), summary_type)()

# Piping one st.cache function into another forms a computation DAG.
summary_type = st.selectbox("Type of summary:", ["sum", "any"])
metadata = load_metadata()
summary = create_summary(metadata, summary_type)
st.write('## Metadata', metadata, '## Summary', summary)