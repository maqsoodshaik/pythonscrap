import scrapping_email as jobfinder
import streamlit as st

if __name__ == "__main__":
    st.title("job finder")
    jobskills = st.text_input(label = "enter the skill name")
    st.write(jobskills)
    st.write(jobfinder.get_jobs(jobskills))