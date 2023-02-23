import os

from dotenv import load_dotenv

load_dotenv()


valid_email = os.getenv("VALID_EMAIL")
valid_password = os.getenv("VALID_PASSWORD")
