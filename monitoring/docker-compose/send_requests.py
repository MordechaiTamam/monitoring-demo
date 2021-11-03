import requests

for i in range(0, 100):
    print(i)
    requests.get("http://localhost:5000/flask-prometheus-grafana-example/")
