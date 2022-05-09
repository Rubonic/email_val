from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask import flash



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/process_email', methods=['POST'])
def process():
    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        'email' : request.form['email']
    }

    user = User.create(data)

    return redirect('/success')


@app.route('/success')
def success():
    user = User.get_last_user()
    flash(f'The email address you entered ({user.email}) is a VALID email address! Thank you!')

    return render_template('success.html', users = User.get_all())
