import requests


api_key = "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"
endpoint = "https://api.openai.com/v1/engines/text-davinci-002/completions"
pregunta = "¿Cuál es el clima de mañana en Nueva York?"

params = {
    "model": "text-davinci-002",
    "prompt": pregunta,
    "max_tokens": 200  
}

headers = {
    "Authorization": f"Bearer {api_key}"
}
response = requests.post(endpoint, headers=headers, json=params)

if response.status_code == 400:
    data = response.json()
    print(data)
else:
    print("No se pudo obtener una respuesta. Código de respuesta:", response.status_code)