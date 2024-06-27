import ollama

########################### LLAMA2 WITH OLLAMA #############################
def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer

def answering(question, character):
    model_version = "wim_model_llama2_13B"
    answer = ""

    answer =ollama.generate(
        model= model_version,
        prompt=f"Assume that you are this person: {character}. Please answer this question about you: {question}",
    )

    print(answer)
    return answer['response']
