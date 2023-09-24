import requests

endpoint='http://127.0.0.1:8000/api/product/1/'
response=requests.get(endpoint,json={"name":"ProductTwo","description":"Product Two","price":100})

print(response.json())
