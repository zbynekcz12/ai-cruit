from backend.llm import run_llm
from backend.prompts import BASIC_INFO_PROMPT, PERSONAL_INFO_PROMPT, QUESTION_GENERATION_PROMPT
from backend.match_score_agent import run_match_score_agent
from backend.constants import PERSONAL_INFO_KEYS
import json


def basic_checker(job_posting, resume_content):
    match_score = run_match_score_agent(job_posting, resume_content)
    
    llm_response = run_llm(BASIC_INFO_PROMPT, {
        "pdf_text": resume_content,
        "job_posting": job_posting
    })
    
    llm_response = json.loads(llm_response)
    llm_response["matching_score"] = match_score
    return llm_response

def get_personal_info(resume_text):
    try:
        llm_response = run_llm(PERSONAL_INFO_PROMPT, {
            "resume_text": resume_text
        })
        resp = json.loads(llm_response)
    except Exception as e:
        print(e)
        resp = {}
    for key in PERSONAL_INFO_KEYS:
        if not resp.get(key):
            resp[key] = []
    return resp

def get_questions(no_of_questions, skill,experience):
    try:
        llm_response = run_llm(QUESTION_GENERATION_PROMPT, {
            "no_of_questions": no_of_questions,
            "skill": skill,
            "experience": experience
        })
        llm_response = json.loads(llm_response)
        return llm_response
    except Exception as e:
        print(e)
        return []