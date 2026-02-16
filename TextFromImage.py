from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What teams are playing in this image, and what sport do they play?",
                },
                {
                    "type": "input_image",
                    "image_url": "https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5663x3709+0+0/resize/900/quality/85/format/webp/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F27%2F52%2Fd81166a04f648f893043d3ef83a4%2Fgettyimages-2198619065.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)