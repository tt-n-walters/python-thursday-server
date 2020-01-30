from flask import Flask

app = Flask(__name__)

@app.route("/logs/<str:name>/<str:log>")
def catch_all(name, log):
    names = ["nico", "lorenzo", "lara", "javier"]
    if name in names:
        logs = ["error", "out"]
        if log in logs:
            with open(f".pm2/logs/{name}-{log}.log", "r") as file:
                return file.read()
        else:
            return "Valid logs are \"error\" or \"out\"."
    else:
        return "Invalid name."

app.run(host="0.0.0.0", port=8888)
