from dotenv import load_dotenv
from mistralai import Mistral
import os

load_dotenv()

mistralai_api_key = os.getenv("MISTRAL_API_KEY")

with Mistral(
    api_key=os.getenv("MISTRAL_API_KEY", mistralai_api_key),
) as mistral:

    res = mistral.chat.complete(model="mistral-small-latest", messages=[
        {
            "content": "Who is the best French painter? Answer in one short sentence.",
            "role": "user",
        },
    ], stream=False)

    # Handle response
    print(res.choices[0].message.content)