import requests

for i in range(0, 10000):
    print(i)
    requests.get("http://localhost:5000/")
