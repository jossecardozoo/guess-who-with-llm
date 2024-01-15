from transformers import pipeline

def get_model():
    # Cargar el modelo BERT preentrenado
    question_answering = pipeline('question-answering', model='bert-base-uncased', tokenizer='bert-base-uncased')

    return question_answering

def ask_wim_model(question, my_character):
    # La idea es que yo le paso al modelo la pregunta, el me indica de que atributo estamos preguntando, y que valor se dice que tiene
    # y aca comparo ese atributo con el del character para ver si concide.
    question_answering = get_model()
    answer = question_answering(question=question, context=my_character)
    return answer

