import os
import json
import random

# Función para procesar un archivo con el formato proporcionado
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Crear un diccionario para almacenar los datos procesados
    data = {}

    for line in lines:
        # Separar la línea en atributo y valor
        attribute_name, value, _amount_of_values = line.strip().split(', ')
        attribute_name = attribute_name.replace('"', '')
        # aca en vez de hacer int(valor) ya hacer el mapeo con una funcion a definir para ya tener todo en strings en mi mega json
        value = int(value)

        # Solo guardar los atributos que me interesan
        if attribute_name in ["eye_color","face_color", "hair_color", "glasses", "glasses_color", "eyebrow_width"]:
            # Agregar al diccionario
            data[attribute_name] = value

    return data

def mapping_int_values_with_string(attribute_name, value):
    # Ruta a donde estan el mapeo de cada valor numerico por cada valor en texto
    json_file_path = 'all_my_values_mapping_attributes.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    return data[attribute_name][value]

# Directorio que contiene tus archivos
directory = os.path.abspath('/Users/anaclara/Desktop/Fing/Tesis/DataSet/cartoonset10k')

# Obtener la lista de archivos en el directorio
files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Crear un diccionario para almacenar todos los datos procesados
all_data = {}

# Procesar cada archivo en la lista y agregar los datos al diccionario principal
for file in files:
    full_path = os.path.join(directory, file)
    attribute_name = os.path.splitext(file)[0]  # Usar el nombre del archivo como atributo
    all_data[attribute_name] = process_file(full_path)
    all_data[attribute_name]['image_file'] = attribute_name

# Convertir el diccionario a formato JSON
json_output = json.dumps(all_data, indent=2)

# Para guardar en un archivo JSON
with open('all_my_characters.json', 'w') as json_file:
    json_file.write(json_output)

