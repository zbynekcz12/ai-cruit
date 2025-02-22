from dotenv import load_dotenv
from langchain_ibm import ChatWatsonx
from langchain_core.prompts import PromptTemplate
import os
from backend.constants import (
    WATSONX_PARAMS,
    WATSONX_MODEL,
    WATSONX_URL
)

load_dotenv()

def run_llm(input_prompt, arguments):

    llm = ChatWatsonx(
        model_id=WATSONX_MODEL,
        url=WATSONX_URL,
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params=WATSONX_PARAMS,
    )
    prompt = PromptTemplate(
        input_variables= list(arguments.keys()),
        template=input_prompt
    )

    chain = prompt | llm

    response = chain.invoke(arguments).content
    return response
