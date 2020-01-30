import argparse
from flask import Flask, request, render_template, Response
from random import choice
from jupiter_flys import generate_seed, jupiter_flys
from user import User
import requests

app = Flask(__name__)


@app.route("/index.html")
def index():
    return "This is a python server. It is awesome."


@app.route("/login")
def login():
    return render_template("login.html", colour="orange", url="/user-info-submit")


@app.route("/signup")
def signup():
    return render_template("signup.html", colour="yellow", url="/user-create")


def doggo_generator():
    api_url = "https://random.dog/woof.json"
    while True:
        result = requests.get(api_url)
        if result.status_code == 200:
            yield result.json()["url"]

# Initiliase the doggo generator
get_dog_url = doggo_generator()

@app.route("/doggos")
def doggos():
    # Bump the generator, and get the next url
    image_url = next(get_dog_url)
    image_or_video = "video" if (image_url.endswith("mp4") or image_url.endswith("webm")) else "img"
    return render_template("dogs.html", url=image_url, image_or_video=image_or_video)


@app.route("/user-info-submit", methods=["POST"])
def user_info_submit():
    content = request.json
    if "username" in content:
        if "password" in content:

            return check_user(content["username"], content["password"])

        else:
            return "You did not submit a password."

    else:
        return "You did not submit a username."


@app.route("/user-create", methods=["POST"])
def user_create():
    content = request.json
    if "username" in content and "password" in content:
        if not content["username"] == "" and not content["password"] == "":
            username = content["username"]
            password = content["password"]
            return create_user(username, password)
        
        return "Invalid username or password."


def create_user(username, password):
    hashed = jupiter_flys(generate_seed(username + password), password)
    new_user = User(username, hashed, "jupiter_flys")
    if not new_user in users:
        users.add(new_user)
        return "Created user successfully."
    else:
        return "That user already exists."
    

users = set()


def check_user(username, password):
    for user in users:
        if user.name == username:
            if user.password == jupiter_flys(generate_seed(username + password), password):
                return "Logged in successfully!"
            else:
                return "Incorrect password."
    return "User not found."


@app.route("/background")
def background():
    colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    chosen_colour = choice(colours)
    return render_template("background.html", colour=chosen_colour)


def load_users():
    with open("users", "r") as file:
        contents = file.read()
    
    
def save_users():
    pass


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
arguments = parser.parse_args()

# Copy the default .htaccess, which contains a default port of 0000
default_path = "public_html/default_htaccess"
with open(default_path, "r") as file:
    contents = file.read()

# Replace the old .htaccess with a new one with the correct port added.
live_path = "public_html/.htaccess"
with open(live_path, "w") as file:
    file.write(contents.replace("0000", str(arguments.port)))

app.run(host="0.0.0.0", port=arguments.port, debug=False)
