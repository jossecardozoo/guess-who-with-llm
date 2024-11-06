import os

from groq import Groq

client = Groq(api_key="")


def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer


def answering(question, character):
    prompt = (f"You are responding to a kid, so be kind and generate short answers. "
              f"You have these physical attributes: {character}. "
              f"You have to answer the question only with a yes or a no. "
              f"Question: {question}")

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    )
    answer = chat_completion.choices[0].message.content
    if (answer == 'undefined'):
        return "I dont understand"
    return answer