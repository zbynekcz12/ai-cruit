import streamlit as st
import pdfplumber
from backend.basic_checker import basic_checker
from backend.candidate import Candidate
import base64

st.markdown(
    """
<style>
    [data-testid="stSidebar"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
    

vert_space = '<div style="marign-top: 2px 5px;"></div>'
st.markdown(vert_space, unsafe_allow_html=True)

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

image_path = "logo.png"
img_base64 = get_base64_image(image_path)

st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{img_base64}" width="130" style="margin-right: 5px;">
        <h1 style="margin: 0;">AI-Cruit</h1>
    </div>
    """,
    unsafe_allow_html=True
)

job_posting = st.text_area(
    "Enter the Job reqirements",
    "",
    height=200,
)

uploaded_file = st.file_uploader("Choose a resume",type=["pdf"],accept_multiple_files=False)
resume_content = None
if uploaded_file is not None:
    # To read file as bytes:
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    resume_content = text


questions_count = st.number_input("Number of questions per skill",min_value=5, max_value=50)

def run_workflow(job_posting, resume_content, questions_count):
    if not job_posting or not resume_content or not questions_count:
        st.error("First Fill all inputs")
        return
    # Job Posting, Resume Reader -> CheckBasic
    basic_response = basic_checker(job_posting, resume_content)
    candidate_object = Candidate()
    candidate_object.name = basic_response["name"]
    candidate_object.experience = basic_response["experience"]
    candidate_object.job_posting = job_posting
    candidate_object.resume_content = resume_content
    candidate_object.question_count = questions_count
    candidate_object.skills = basic_response["skills"]
    candidate_object.matching_score = basic_response["matching_score"]
    candidate_object.summary = basic_response["summary"]
    
    # # save this object in session
    st.session_state["current_candidate"] = candidate_object
    st.switch_page("pages/analysis.py")


if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        run_workflow(job_posting, resume_content, questions_count)