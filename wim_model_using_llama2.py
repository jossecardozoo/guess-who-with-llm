import replicate

########################### LLAMA2 WITH REPLICATE #############################
def ask_wim_model(question, character):
    answer = answering(question, character)
    return answer

def answering(question, character):
# The meta/llama-2-70b-chat model can stream output as it's running.
    model_version = "meta/llama-2-70b-chat"

    for event in replicate.stream(
        model_version,
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 1,
            "prompt": f"Pleas answer this question about the character: {question}",
            "temperature": 0.5,
            "system_prompt": f"You are a helpful, respectful and honest assistant. You have this phisical attributes: {character}. You have to answer the question without reveling the correct value of the attributes",
            "max_new_tokens": 10,
            "min_new_tokens": -1
        },
    ):
        print(str(event), end="")

# character = "eye color is green, face color is black, hair color is blue, i have glasses, my glasses color is black"
# answering("Are your eyes green?",character)
