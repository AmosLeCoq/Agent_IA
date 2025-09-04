import requests

r = requests.get("http://10.229.43.154:11434/api/tags")
print(r.json())