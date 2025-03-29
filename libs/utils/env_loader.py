from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    return {k: os.getenv(k) for k in os.environ.keys()}