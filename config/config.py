from dotenv import load_dotenv
import os

load_dotenv()

class config:
    BaseUrl=os.getenv("baseUrl")
    userName=os.getenv("userName")
    password=os.getenv("password")