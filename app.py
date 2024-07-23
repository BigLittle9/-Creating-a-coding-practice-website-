from flask import Flask, render_template, request, redirect, session
import os
import ast

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load questions and answers from a file or database
questions = [
    {
        'question': 'Write a function to add two numbers:',
        'expected_output': '5'
    },
    {
        'question': 'Write a function to reverse a string:',
        'expected_output': '"olleh"'
    },
    # Add more questions here
]

# Load user points from a file or database
user_points = {}
user_answered_questions = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password are valid
        if username in user_points:
            session['user'] = username
            if username not in user_answered_questions:
                user_answered_questions[username] = []
            return redirect('/question')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username is unique
        if username not in user_points:
            user_points[username] = 0
            user_answered_questions[username] = []
            # Save the new user to a file or database
            return redirect('/login')
        else:
            return render_template('register.html', error='Username already exists')
    return render_template('register.html')

@app.route('/question', methods=['GET', 'POST'])
@app.route('/question', methods=['GET', 'POST'])

@app.route('/question', methods=['GET', 'POST'])

@app.route('/question', methods=['GET', 'POST'])
@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        if 'skip' in request.form:
            # Skip the current question
            session['current_question'] = next((i for i in range(len(questions)) if i not in user_answered_questions.get(session['user'], [])), None)
            if session['current_question'] is None:
                return render_template('question.html', message='Congratulations! You have answered all the questions.')
            return redirect('/question')
        else:
            user_input = request.form['user_input']
            # Execute the user's input as Python code and get the output
            try:
                output = ''
                exec('output = ' + user_input)
                output = str(output)
            except Exception as e:
                return render_template('question.html', question=questions[session['current_question']], points=user_points[session['user']], error=str(e))

            # Check if the output matches the expected output
            current_question = questions[session['current_question']]
            if output == current_question['expected_output']:
                user_points[session['user']] += 1
                user_answered_questions[session['user']].append(session['current_question'])
                # Save the updated user points and answered questions to a file or database
                if len(user_answered_questions[session['user']]) == len(questions):
                    return render_template('question.html', message='Congratulations! You have answered all the questions.')
                else:
                    session['current_question'] = next((i for i in range(len(questions)) if i not in user_answered_questions[session['user']]), None)
                    if session['current_question'] is None:
                        return render_template('question.html', message='Congratulations! You have answered all the questions.')
                    return render_template('question.html', question=questions[session['current_question']], points=user_points[session['user']], show_skip=True)
            else:
                return render_template('question.html', question=current_question, points=user_points[session['user']], error='Incorrect answer', show_skip=True)
    else:
        if 'current_question' not in session or session['current_question'] is None:
            session['current_question'] = next((i for i in range(len(questions)) if i not in user_answered_questions.get(session['user'], [])), None)
            if session['current_question'] is None:
                return render_template('question.html', message='Congratulations! You have answered all the questions.')
        return render_template('question.html', question=questions[session['current_question']], points=user_points.get(session['user'], 0), show_skip=len(user_answered_questions.get(session['user'], [])) < len(questions))

@app.route('/leaderboard')
def leaderboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('leaderboard.html', user_points=user_points)

if __name__ == '__main__':
    app.run()