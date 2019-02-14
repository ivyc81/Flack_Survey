from flask import Flask, request, session, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "the-secret-key"

debug = DebugToolbarExtension(app)

surveys["satisfaction"]

@app.route("/")
def show_start_survey():
    """ creates the satisfaction survey form"""

    return render_template("landing.html", survey_title = surveys["satisfaction"].title, survey_instruction = surveys["satisfaction"].instructions)

@app.route("/", methods=["POST"])
def show_satisfaction_survey():
    """ creates the satisfaction survey form"""

    return render_template("landing.html", survey_title = surveys["satisfaction"].title, survey_instruction = surveys["satisfaction"].instructions)
