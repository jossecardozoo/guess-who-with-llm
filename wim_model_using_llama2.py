import replicate

########################### LLAMA2 WITH REPLICATE #############################
def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer

def answering(question, character):
    model_version = "meta/llama-2-70b-chat"
    answer = ""

    for event in replicate.stream(
        model_version,
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 1,
            "prompt": f"Pleas answer this question about the character: {question}",
            "temperature": 0.001,
            "system_prompt": f"You are responding to a kid, so be kind and generate short answers. You have this phisical attributes: {character}. You have to answer the question only with a yes or a no",
            "max_new_tokens": 25,
            "min_new_tokens": -1
        },
    ):
        answer = answer + str(event) + ""

    # Por alguna razon el modelo retorna parte de la respuesta anterior.
    # Esto es para solo obtener la ultima respuesta, habria que mejorarlo
    answer_words = answer.split()
    return answer_words[-1]
