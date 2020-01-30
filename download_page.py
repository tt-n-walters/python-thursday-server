import requests

r = requests.get("https://pythonavanzado.techtalents.cloud/snippets/login.html")

if r.status_code == 200:
    with open("login.html", "w") as file:
        file.write(r.text)
