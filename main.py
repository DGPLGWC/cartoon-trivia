import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html')

@app.route('/question/<int:question_id>')
def question(question_id):
    return render_template(
        'questions/%s.html' % str(question_id))

@app.route('/error')
def error():
    return render_template(
        'error.html')

@app.route('/success')
def success():
    return render_template(
        'success.html')

@app.route('/about')
def about():
    return render_template(
        'about.html')

@app.route('/questions/<string:answer>/<int:question_id>')
def questions( answer, question_id ):
    try:
        score = 0
        if question_id == 1:
            question_id += 1
            if answer == "Steamboat Willy":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="Streamboat Willy",
                    next=question_id)
        elif question_id == 2:
            question_id += 1
            if answer == "Norway":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="Norway",
                    next=question_id)
        elif question_id == 3:
            question_id += 1
            if answer == "Bambi":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="Bambi",
                    next=question_id)
        elif question_id == 4:
            question_id += 1
            if answer == "A fork":
                score += 1
                return render_template(
                    'success.html',
                    next=question_id,
                    score=score)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="A fork",
                    next=question_id)
        elif question_id == 5:
            if answer == "May 5th, 2006":
                score += 1
                return render_template(
                    'success.html',
                    score=score,
                    finished=True)
            else:
                return render_template(
                    'error.html',
                    correctAnswer="May 5th, 2006",
                    finished=True)

    except ValueError:
        print 'Oops thats an error should be caught'

# app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))