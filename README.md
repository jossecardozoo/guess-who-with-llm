# Versión del juego “Guess who?” usando un LLM
Este documento presenta un primer prototipo del juego “Guess who?” implementado utilizando un modelo de lenguaje de gran tamaño (LLM). Este proyecto fue desarrollado como parte del trabajo final para el grado de Licenciatura en Computación.


## Requisitos

Para correr la aplicación, asegúrate de tener instalados los siguientes requisitos:

- [Python](https://www.python.org/downloads/) (versión recomendada: 3.10.6)
- [Dependencias](#dependencias)

## Instrucciones de Uso

### 1. Ejecutar la Aplicación

Para iniciar la aplicación, es necesario correr el archivo `api.py`:

```bash
python api.py
```

### 2. Archivo de Contexto y Comunicación
- `wim_simple_chat.py`: Este archivo mantiene el contexto de la aplicación, define los candidatos y se comunica con el modelo.

### 3. Comunicación con el Modelo
Dependiendo de si deseas usar el modelo localmente o a través de Replicate, utiliza uno de los siguientes archivos:
- `wim_llama2_model_locally.py`: Para uso local. Este archivo fue probado con [Ollama](https://ollama.com/library/llama2:13b).
- `wim_llama2_model_replicate.py`: Para uso con Replicate. Para utilizar Replicate, es necesario crear una cuenta y obtener un token de autenticación. Más información para realizar esto se encuentra aquí: [Guía para Fine-Tune Llama-2 en Replicate](https://replicate.com/blog/fine-tune-llama-2).

### 4. Generar el Archivo de Personajes
Para generar un nuevo archivo `all_my_characters.json`, que contiene los atributos de los personajes y el nombre del archivo de su imagen, utiliza el archivo `wim_characters_loading.py`. Asegúrate de agregar la ruta completa de el lugar en donde te descargaste el [CartoonSet](https://google.github.io/cartoonset/) en tu computadora para que el JSON se genere correctamente.

```bash
python wim_characters_loading.py
```

### Dependencias
Asegúrate de instalar las siguientes dependencias listadas en `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Notas Adicionales
Configuración de Replicate: Sigue las instrucciones en el enlace proporcionado antes para obtener tu token de autenticación.
