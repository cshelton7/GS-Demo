import os
#from google.oauth2 import id_token
#from google.auth.transport import requests
import flask
from flask import Flask, render_template, redirect, flash, request, json, session
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# Code from project milestones

# point to heroku database
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# remove a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# read information from secrets file
#CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']


@app.route("/", methods=["GET", "POST"])
def login():
    """
    Login page of application
    """
    return render_template("login.html")

# validate user
#@app.route('/verify', methods=['POST'])
#def verify():
   # id_token = json.loads(flask.request.data)
   # try:
        # Specify the CLIENT_ID of the app that accesses the backend:
      #  idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

    # ID token is valid. Get the user's Google Account ID from the decoded token.
     #   userid = idinfo['sub']
   # except ValueError:
        # Invalid token
     #   pass

@app.route("/home", methods=["GET", "POST"])
def home():
    """
    Home page of application
    """
    if flask.request.method == "POST":
        name = json.loads(flask.request.data)
        return flask.redirect(flask.url_for("home"))
    return render_template(
        "home.html",
        user = name,
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), 
        port=int(os.getenv("PORT", 8080)), 
        debug=True
    )