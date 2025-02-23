import os
from dotenv import load_dotenv
from langchain_ibm import ChatWatsonx
from langchain_core.prompts import PromptTemplate
from backend.constants import (
    WATSONX_PARAMS,
    WATSONX_MODEL,
    WATSONX_URL
)

load_dotenv()

def run_llm(input_prompt, arguments):
    """
    Run the LLM with the given input prompt and arguments.

    Args:
        input_prompt (str): The input prompt to the LLM.
        arguments (dict): The arguments to the input prompt.

    Returns:
        str: The response from the LLM.

    Raises:
        Exception: If there is an error running the LLM.
    """

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
