import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Get and store the api key from .env
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create instance of Gemini client
    client = genai.Client(api_key=api_key)

    # Gemini model to use
    model = "gemini-2.0-flash-001"

    # Content to send the model
    prompt = sys.argv[1]

    # Checks if verbose was sent
    verbose = "--verbose" in sys.argv

    # Store messages for later use
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    # Send back the prompt to user if verbose
    if verbose:
        print(f'User Prompt: {prompt}')

    # Send variables to response function
    get_response(client, model, messages, verbose)

def get_response(client, model, messages, verbose):
    # Send content and generate reponse
    response = client.models.generate_content(model=model, contents=messages)

    # Print extra data if verbose
    if verbose:
        print(f'Prompt Token Count: {response.usage_metadata.prompt_token_count}')
        print(f'Candidates Token Count: {response.usage_metadata.candidates_token_count}')
    
    # Always print no matter what
    print(f'\nResponse: \n\n{response.text}')

if __name__ == "__main__":
    main()