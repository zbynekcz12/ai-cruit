BASIC_INFO_PROMPT = """
I'm evaluating the resume of candidate. so your task is to analyze the content of resume that i'm providing you.
Resume : {pdf_text} 
Job requirements: {job_posting}
you have to give response int the following JSON format:
{{
    "name": Name of the candidate,
    "experience": how much experience the candidate has in industry only in years e.g. 1+ year, 2+ years, 3+ years etc.
    "skills": technical skills the candidate has. your response should be like array ["python","c++","java"]
    "summary": analyze the resume and match with job requirements and give summary for why we ahould hire this candidate and if any negative point you found that also mentioned in summary.just give me 3-4 point in summary. bold the important keywords and summary format in array ["point 1", "point 2", ....].
}}

If you not found any of the above information in resume then make it empty "".
your response is only in JSON format not contain any other text.
"""

PERSONAL_INFO_PROMPT = """Consider yourself as an expert resume reviewer. I am giving you the resume text:

{resume_text}

I want to give this resume information to the recruiter so first read and understand the resume properly and then give me the output in the following format:

{{
"company_wise_experience" : [{{"company_name": "The name of the company", "job_location": "Job location of the role", "role": "Job role in the company", "duration": "Start month start year - End month end year"}}, ...],

"education": [{{"insitution_name": "Name of the school or university or college", "grade":"Grade in the corresponding institution"}}, ...],
"personal_information": [{{"category": "Personal Information category like email, github, Phone number etc.", "value": "Value of the corresponding category"}}, ...],
"achievements": [{{"category": "achievement category", "description":"Detailed description of the achievement category"}}, ...],
"certification": ["Name of the certification that user has done", ...]
}}

Make sure that you only give JSON in the output.

Also make sure that you did not miss any key in the above JSON."""

QUESTION_GENERATION_PROMPT="""
I'm evaluating the resume of candidate.
I'm providing you no.of questions to be generted.
No. of Questions : {no_of_questions}
Skill : {skill}

You have to generate {no_of_questions} questions on {skill} skill. Candidate has an overall {experience} of experience.
So consider the candidate experience and based on that generate best question for interview purpose.
And also give me related answer for that question also.

you must have to give response into the list of JSON format:
[
    {{"question": "Question 1", "answer": "Answer 1"}},
    {{"question": "Question 2", "answer": "Answer 2"}},
    {{"question": "Question 3", "answer": "Answer 3"}},
    ....
]
"""