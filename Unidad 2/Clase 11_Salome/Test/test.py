import requests

response = requests.get("https://localhost:8000")



data = {
    "marca":"Prueba Marca",
    "sabor":"Prueba Sabor",
    "color":"Prueba Color",
    "cantidad":12
}

response = requests.post("http://127.0.0.1:8000/v1/papitas", data=data)

print(response.status_code)
print(response.content)
