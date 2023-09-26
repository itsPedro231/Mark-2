import openai

openai.api_key = "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"

def gpt(input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[   
            {
                "role": "system",
                "content": """
                Your name is Mark. 
                Behavelike JARVIS from Iron Man.
                Never mention that you behave like jarvis.
                Never mention you are an AI.
                If asked who created you, say it was Pedro.
                Always fit a "sir" in your responses.
                """
            },
            {
                "role": "user",
                "content": input
            }
            ],
        temperature=0.5,
        max_tokens=256
    )
    output = response["choices"][0]["message"]["content"]
    print(output)
    return output

"""
response model
{
  "id": "chatcmpl-82k0YazmDGvXMC0LvMX9RoKiHqL01",
  "object": "chat.completion",
  "created": 1695664202,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 9,
    "total_tokens": 28
  }
}
"""