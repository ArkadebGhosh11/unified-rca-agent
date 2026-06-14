from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

if key:
    print("API Key Loaded Successfully")
    print(f"Key Prefix: {key[:10]}...")
else:
    print("API Key Not Found")