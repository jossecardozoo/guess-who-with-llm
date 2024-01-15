import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def get_data():
    data = {
        {
            "eye_color": 3,
            "face_color": 10,
            "hair_color": 4,
            "character_number": "c1"
        },
        {
            "eye_color": 2,
            "face_color": 1,
            "hair_color": 3,
            "character_number": "c2"
        },{
            "eye_color": 0,
            "face_color": 8,
            "hair_color": 1,
            "character_number": "c3"
        },{
            "eye_color": 3,
            "face_color": 5,
            "hair_color": 4,
            "character_number": "c4"
        },
    }
    
    df = pd.DataFrame(data)
    print(df)

    return df

def train_model():
    # Falta procesar mi data set para que quede cada ejemplo con un formato de este estilo, por ahora usar este ejemplo
    data = get_data()
    




def ask_wim_model(processed_question, my_character):
    # La idea es que yo le paso al modelo la pregunta, el me indica de que atributo estamos preguntando, y que valor se dice que tiene
    # y aca comparo ese atributo con el del character para ver si concide.
    return True