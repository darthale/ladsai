import logging
import os
import streamlit as st
import boto3

def init_logging():
    logging.basicConfig(format="[%(asctime)s] %(levelname)+8s: %(message)s")
    local_logger = logging.getLogger()
    local_logger.setLevel(logging.INFO)
    return local_logger

logger = init_logging()

if os.environ.get("LOCAL_RUN"):
    s3a_access_key = os.environ.get("s3aAccessKey")
    s3a_secret_key = os.environ.get("s3aSecretKey")
else:
    s3a_access_key = st.secrets["s3aAccessKey"]
    s3a_secret_key = st.secrets["s3aSecretKey"]

def get_logger():
    return logger


def fetch_prompt_config(prompt_config_path: str, bucket_name: str = "px-ladsai-poc"):
    recommendation_prompt = ""

    if os.environ.get("LOCAL_RUN"):
        recommendation_prompt = open(prompt_config_path[0], "r").read()
    else:
        # Initialize the S3 client
        s3_client = boto3.client('s3', aws_access_key_id=s3a_access_key, aws_secret_access_key=s3a_secret_key)
        try:
            response = s3_client.get_object(Bucket=bucket_name, Key=prompt_config_path[1])
            recommendation_prompt = response['Body'].read().decode('utf-8')  # Decode the file content as a string
        except Exception as e:
            logger.exception(f"Error fetching the file from S3")

    return recommendation_prompt