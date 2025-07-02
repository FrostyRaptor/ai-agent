import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    # Get and store the api key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create instance of Gemini client
    client = genai.Client(api_key=api_key)

    # Gemini model to use
    model = "gemini-2.0-flash-001"

    # Content to send the model
    content = sys.argv[1]

    # Send variables to response function
    get_response(client, model, content)

def get_response(client, model, content):
    # Send content and generate reponse
    response = client.models.generate_content(model=model, contents=content)

    print(response.text)
    print(response.usage_metadata.prompt_token_count)
    print(response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()