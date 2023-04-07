import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Harry Potter was mid'


@app.route('/')
def landing_page():
    # STATIC WELCOME PAGE
    return render_template('index.html')


@app.route('/submit', methods=["GET", "POST"])
def process_submission():
    # USER SUBMITTED INFO. SAVE IT IN SESSION AND LOAD RESULTS PAGE
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return render_template('results.html')


@app.route('/destroy_session')
def reset_session():
    # RESET SESSION COOKIES AND REDIRECT TO '/'
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
