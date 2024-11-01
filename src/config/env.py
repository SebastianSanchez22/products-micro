import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CREDENTIALS = os.getenv('DATABASE_CREDENTIALS')