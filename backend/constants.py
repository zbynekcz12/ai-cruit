WATSONX_URL="https://us-south.ml.cloud.ibm.com"
WATSONX_PARAMS={
    "temperature": 0,
    "max_tokens": 8000,
}
WATSONX_MODEL = "ibm/granite-3-8b-instruct"
PERSONAL_INFO_KEYS = ["company_wise_experience", "education", "personal_information", "achievements", "description", "certification"]


EXPERIENCE_COL = ["Company Name", "Job Location", "Role", "Duration"]
EXPERIENCE_COL_KEY = ["company_name", "job_location", "role", "duration"]

EDUCATION_COL = ["Institution Name", "Grade"]
EDUCATION_COL_KEYS = ["institution_name", "grade"]

ACHIEVEMENTS_COL = ["Category", "Description"]
ACHIEVEMENTS_COL_KEY = ["category", "description"]

CERTIFICATION_COL = ["Certifications"]
CERTIFICATION_COL_KEY = []