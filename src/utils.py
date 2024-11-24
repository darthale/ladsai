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

def build_vada(vada_file_path: str):

    # Ensure the environment variables are set
    if not s3a_access_key or not s3a_secret_key:
        raise ValueError("Environment variables 's3aAccessKey' and 's3aSecretKey' must be set.")

    # Read the text file content
    with open(vada_file_path, "r") as file:
        content = file.read()

    # Replace placeholders with environment variable values
    content = content.replace("{s3aAccessKey}", s3a_access_key)
    content = content.replace("{s3aSecretKey}", s3a_secret_key)

    # Save the updated content to a new file or overwrite the existing file
    tmp_file_path = vada_file_path + ".tmp"
    with open(tmp_file_path, "w") as file:
        file.write(content)
    
    return tmp_file_path


def fetch_prompt_config(prompt_config_path: str, bucket_name: str = "px-ladsai-poc"):
    angel_recommendation_prompt = ""

    if os.environ.get("LOCAL_RUN"):
        angel_recommendation_prompt = open(prompt_config_path[0], "r").read()
    else:
        # Initialize the S3 client
        s3_client = boto3.client('s3', aws_access_key_id=s3a_access_key, aws_secret_access_key=s3a_secret_key)
        try:
            response = s3_client.get_object(Bucket=bucket_name, Key=prompt_config_path[1])
            angel_recommendation_prompt = response['Body'].read().decode('utf-8')  # Decode the file content as a string
        except Exception as e:
            logger.exception(f"Error fetching the file from S3")

    return angel_recommendation_prompt