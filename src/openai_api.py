from openai import OpenAI
import os
import streamlit as st

from src.utils import get_logger

logger = get_logger()

def create_assistants_client():
    logger.info("Creating OpenAI client")
    if os.environ.get("LOCAL_RUN"):
        openai_client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"]
        )
    else:
        openai_client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

    return openai_client

client: OpenAI = create_assistants_client()


def get_client():
    return client