# auth.py
import os
from dotenv import load_dotenv

load_dotenv()

# Set Google Application Credentials
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if GOOGLE_CREDENTIALS_PATH:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS_PATH
else:
    raise ValueError("Please set GOOGLE_APPLICATION_CREDENTIALS in your .env file")
