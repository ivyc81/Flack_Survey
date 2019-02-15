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

    session['responses'] = []

    return render_template("landing.html", survey_title=surveys["satisfaction"].title, survey_instruction=surveys["satisfaction"].instructions)


@app.route("/questions/<int:question_number>", methods=["POST"])
def show_satisfaction_survey(question_number):
    """ creates the satisfaction survey form """

    question = surveys["satisfaction"].questions[question_number]

    question_string_list = [question.question, question.choices[0], question.choices[1]]

    next_question = question_number + 1

    return render_template("form.html", survey_title=surveys["satisfaction"].title, survey_instruction=surveys["satisfaction"].instructions, question=question_string_list, next_question = next_question)