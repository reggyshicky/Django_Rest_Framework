import requests

response = requests.get('http://127.0.0.1:8000/drinks') #leave the application running
print(response.json())
