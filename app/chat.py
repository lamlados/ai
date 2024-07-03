import os
from config import myenv, SYSTEM_PROMPT
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
)

def get_response(conversation_history, is_streaming=False):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=conversation_history,
        stream=is_streaming
    )
    return response if is_streaming else response.choices[0].message.content

def print_response(prompt, conversation_history, is_streaming):
    conversation_history.append({"role": "user", "content": prompt})
    if is_streaming:
        for chunk in get_response(conversation_history, is_streaming):
            print(chunk.choices[0].delta.content or "", end="")
            conversation_history.append({"role": "assistant", "content": chunk.choices[0].delta.content})
    else:
        response = get_response(conversation_history)
        print(response)
        conversation_history.append({"role": "assistant", "content": response})

def start_conversation():
    conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting conversation.")
            break
        print_response(user_input, conversation_history, is_streaming=False)