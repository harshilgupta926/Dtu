from google import genai
from .env import API_KEY

while True:
    client = genai.Client(api_key=API_KEY)
    master_prompt = """
    You are an expert venture capital analyst and startup pitch coach. Your objective is to take unstructured, rambling inputs from founders seeking investors (or investors seeking opportunities) and transform them into a clean, concise, investment-ready pitch.

    ### Rules & Behavior:
    1. NO FLUFF, NO COMMENTARY: Do not include conversational filler. Output only the structured categories.
    2. MISSING DATA HANDLING: If critical details are missing, list them first as targeted questions.
    3. OUTPUT FORMAT: Organize the response strictly into:
    - [MISSING DATA]
    - [INDUSTRY / SECTOR]
    - [STAGE]
    - [THE ASK]
    - [CORE OBJECTIVE / VALUE PROP]
    - [CLEANED PITCH]
    """

    config = types.GenerateContentConfig(
    system_instruction=master_prompt,
    temperature=0.1,
    max_output_tokens=500,
    )

    user_query = input("Please enter your pitch or investment opportunity details: ")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_query,
        config=config,
    )

    print(response.text)
