import requests

endpoint='http://127.0.0.1:8000/api/product/'
response=requests.post(endpoint,json={"name":"ProductTwo","description":"Product Two","price":100})

print(response.json())
