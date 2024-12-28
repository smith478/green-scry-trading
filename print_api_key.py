from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('groq_api.env')

# Access the API key
groq_api_key = os.getenv('GROQ_API_KEY')

# Example usage of the API key
print(f"Groq API Key: {groq_api_key}")