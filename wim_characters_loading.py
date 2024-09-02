import os
import json

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

        # Solo guardar los atributos que me interesan
        if attribute_name in ["eye_color","face_color", "hair_color", "glasses", "glasses_color", "eyebrow_width"]:
            # Agregar al diccionario
            string_value = mapping_int_values_with_string(attribute_name, value)
            data[attribute_name] = string_value

    return data

def mapping_int_values_with_string(attribute_name, value):
    # Ruta a donde esta el mapeo de cada valor numerico por cada valor en texto
    json_file_path = 'all_my_values_mapping_attributes.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    return data[str(attribute_name)][str(value)]

# Directorio que contiene tus archivos
directory = os.path.abspath('/cartoonset10k')

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

