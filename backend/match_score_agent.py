import os
import asyncio
import re
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_watsonx_client.config import WatsonxClientConfiguration
from autogen_watsonx_client.client import WatsonXChatCompletionClient
from backend.constants import WATSONX_URL, WATSONX_MODEL
from dotenv import load_dotenv

load_dotenv()

def extract_percentage(text):
    match = re.search(r'(\d+)%', text)
    if match:
        return int(match.group(1))
    else:
        return None

async def main(job_posting, resume_content):
    wx_config = WatsonxClientConfiguration(
        model_id=WATSONX_MODEL, 
        api_key= os.getenv("WATSONX_APIKEY"),
        url=WATSONX_URL,
        project_id=os.getenv("WATSONX_PROJECT_ID")
    )

    wx_client = WatsonXChatCompletionClient(**wx_config)

    primary_agent = AssistantAgent(
        "primary",
        model_client=wx_client,
        system_message="You are a helpful AI assistant.Find matching score between job requiremnets and resume of the candidate",
    )

    critic_agent = AssistantAgent(
        "critic",
        model_client=wx_client,
        system_message="Provide constructive feedback. analyze the matching score whether it is reliable or not. if you feel it is not correct then 'REJECT' it .Respond with 'APPROVE' and with matching score to when your feedbacks are addressed.",
    )

    text_termination = TextMentionTermination("APPROVE")

    team = RoundRobinGroupChat([primary_agent, critic_agent], termination_condition=text_termination)
    
    matching_score = ""
    async for message in team.run_stream(task=f"""Your task is to find the Matching score. 
    I am providing you the Job requirements and resume of the candidate. 
    you have to analyze the job requirements and then observing skills, experience, achievemnets and certifications in resume.
    based on that you have to decide how much % resume is matched with our job requirements. 
    and give me final response only in percentage no other text.
    Job requirements: {job_posting}
    Resume : {resume_content}
    """):
        if isinstance(message, TaskResult):
            pass
        else:
            matching_score= message.content
            
    return extract_percentage(matching_score)

def run_match_score_agent(job_posting, resume_content):
    score = asyncio.run(main(job_posting, resume_content))
    return score

