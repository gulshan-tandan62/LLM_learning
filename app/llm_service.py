from google import genai
from config import get_api_key
from google.genai import types
from prompt_service import build_system_instruction
def generate_response(user_input,mode="general",level="Beginner"):
    api_key = get_api_key()

    client = genai.Client(api_key=api_key)

    system_instruction=build_system_instruction(
        mode=mode,
        level=level
    )
  

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction
        )
    )
    if not response.text:
        raise ValueError("gemini returned an empty response.")

    return response.text