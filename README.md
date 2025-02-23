# AI-Powered Resume Analysis and Job Matching

This project analyzes candidate resumes using AI and provides an efficient way to match resumes with job descriptions, extract candidate information, and generate interview questions. The system uses AutoGen’s agent functionality where two agents collaborate to provide the most relevant match score. We also use Streamlit for the user interface.

## Features
- **Resume Analysis:** Extracts education, experience, achievements, contact details, and skills from resumes.
- **Job Match Score:** Compares the job description with the resume and calculates a match percentage.
- **Skill-Based Interview Questions:** Allows recruiters to generate interview questions for specific skills and provides model-generated answers.
- **Candidate Summary:** Summarizes key information from the resume.

## Technologies Used
- Python
- IBM granite-3-8b-instruct LLM
- Langchain
- AutoGen
- Streamlit

## Setup Instructions

### Prerequisites
Make sure you have Python installed.

### Clone the Repository
```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### Install Dependencies
All dependencies are listed in the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the `backend` folder of the project and add your WatsonX project ID and API key:
```
WATSONX_PROJECT_ID=your-project-id
WATSONX_APIKEY=your-api-key
```

### Run the Application
Launch the Streamlit UI with the following command:
```bash
streamlit run app.py
```

## Usage
1. Open the application using the Streamlit command above.
2. Upload the job description and resume files.
3. Enter the number of interview questions required.
4. View extracted candidate information, match score, interview questions, and answers.
5. Get a summarized candidate profile.


