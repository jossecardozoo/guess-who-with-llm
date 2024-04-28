import ollama

########################### LLAMA2 WITH OLLAMA #############################
def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer

def answering(question, character):
    model_version = "llama2"    
    answer = ""

    answer =ollama.generate(
        model= model_version,
        prompt=f"Assume that you are this person: {character}.Pleas answer this question about you: {question}",
        system=f"You are responding to a kid, so be kind and generate short answers. You have to answer the question only with a yes or a no",

        options={
            "top_k": 20,
            "top_p": 0.8,
            "temperature": 0.001,
        }
        # input={
        #     "debug": False,
        #     "top_k": 50,
        #     "top_p": 1,
        #     "prompt": f"Pleas answer this question about the character: {question}",
        #     "temperature": 0.001,
        #     "system_prompt": f"You are responding to a kid, so be kind and generate short answers. You have this phisical attributes: {character}. You have to answer the question only with a yes or a no",
        #     "max_new_tokens": 25,
        #     "min_new_tokens": -1,
        #     # "length_penalty":0.1
        # },
    )

    print(answer)
    return answer['response']

# character = "The person has green eyes, black skin, and blue hair. They are wearing yellow glasses."
# answering("Are your eyes green?", character)

# "system_prompt": "You are responding to a kid, so be kind and use simple lenguaje. You have this phisical attributes: {character}. You have to answer the question with yes or no",
