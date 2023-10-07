import requests
import json

api_key = "tu_clave_de_API_de_OpenAI"
endpoint = "https://api.openai.com/v1/engines/davinci/completions"
pregunta = "¿Cuánto es 1 + 1?"

params = {
    "prompt": pregunta,
    "max_tokens": 50,
    "temperature": 0.7
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(endpoint, headers=headers, json=params)
data = response.json()

respuesta = data["choices"][0]["text"].strip()
print("Respuesta de ChatGPT:", respuesta)