import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./env")
DEBUG = os.getenv("DEBUG")


