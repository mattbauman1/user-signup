from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

def username_verification(username):
    if username == "":
        return '"Username" cannot be blank!'
    elif re.match("^[a-zA-Z0-9-_.]{3,20}$", username) == None:
        return 'The "Username" must be between 3 and 20 characters in length and can have no special characters or spaces.'
    else:
        return ""

def password_verification(password):
    if password == "":
        return '"Password" cannot be blank!'
    elif re.match("^[a-zA-Z0-9-_.]{3,20}$", password) == None:
        return 'The "Password" must be between 3 and 20 characters in length and can have no special characters or spaces'
    else:
        return ""

def verifypassword_verification(password, verifypassword):
    if verifypassword == "":
        return 'You must retype your "Password" here!'
    elif password != verifypassword:
        return "The passwords you entered do not match, please try again!"
    else:
        return ""

def email_verification(email):
    if re.match("^[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+\.[a-zA-Z]{3,20}", email) == None:
        return "You entered an invalid e-mail, please try again!"
    else:
        return ""

@app.route('/', methods=['POST'])
def verify():
    username = request.form.get("username")
    password = request.form.get("password")
    verifypassword = request.form.get("verifypassword")
    email = request.form.get("email")
    adjustable_username_error = username_verification(username)
    adjustable_password_error = password_verification(password)
    adjustable_verifypassword_error = verifypassword_verification(password, verifypassword)
    adjustable_email_error = email_verification(email)
    if adjustable_username_error != "" or adjustable_password_error != "" or adjustable_verifypassword_error != "" or adjustable_email_error != "":
        return render_template('index.html', old_username_value = username, old_email_value = email, username_error = adjustable_username_error, password_error = adjustable_password_error, verifypassword_error = adjustable_verifypassword_error, email_error = adjustable_email_error)
    else:
        return redirect("/welcome?name=" + username)

@app.route('/welcome', methods = ['GET'])
def welcome():
    return render_template('welcome.html', name = request.args.get("name"))

app.run()
