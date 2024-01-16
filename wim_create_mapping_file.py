import json

# Tu JSON inicial
initial_json = {
    "eye_color":{},
    "face_color":{},
    "hair_color":{},
    "glasses":{},
    "glasses_color":{},
    "eyebrow_width":{}
}

# Diccionario de incrementos para cada atributo
increments = {
    "eye_color": 5,
    "face_color": 11,
    "hair_color": 10,
    "glasses": 12,
    "glasses_color": 7,
    "eyebrow_width": 3
}

# Llenar el JSON con claves y valores
for attribute, limit in increments.items():
    initial_json[attribute] = {str(i): "algo" for i in range(limit + 1)}

# Imprimir el JSON actualizado
print(initial_json)

# Para guardar en un archivo JSON
json_output = json.dumps(initial_json,indent=2)

with open('all_my_values_mapping_attributes.json', 'w') as json_file:
    json_file.write(json_output)