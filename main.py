import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pf import generate_report


st.set_page_config(
    page_title="On time Analysis in HealthCare Management System", page_icon=":hospital:")
st.markdown("""
<style>
    #MainMenu,
    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


st.title('On time Analysis in HealthCare Management System')
st.markdown("""
Python librarries that are used
* *Python libraries:* pandas, streamlit, numpy, matplotlib, seaborn
* *Data source:* Dataset from kaggle.com
""")
upload_file = st.file_uploader('Upload a file containing hospital data')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df.describe())
    generate_report(df=df)
    st.markdown("""
    <a href='http://127.0.0.1:5500/output.html' target='_blank'>View Report</a>
    """, unsafe_allow_html=True)

st.markdown(open("output.html", encoding="utf8").read(),
            unsafe_allow_html=True)
