import ollama

########################### LLAMA2 WITH OLLAMA #############################
def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer

def answering(question, character):
    model_version = "wim_model_llama2:13b"
    answer = ""

    answer =ollama.generate(
        model= model_version,
        # system=f"You are responding to a kid, so be kind and generate short answers. You have to answer the question with a yes or a no, without reveling the correct answer",
        prompt=f"Assume that you are this person: {character}.Pleas answer this question about you: {question}",
        # options={
        #     "top_k": 20,
        #     "top_p": 0.7,
        #     "temperature": 0.001,
        # }
    )

    print(answer)
    return answer['response']

# character = "The person has green eyes, black skin, and blue hair. They are wearing yellow glasses."
# answering("Are your eyes green?", character)

# "system_prompt": "You are responding to a kid, so be kind and use simple lenguaje. You have this phisical attributes: {character}. You have to answer the question with yes or no",
