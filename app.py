from flask import Flask, request, render_template, url_for

app = Flask(__name__)

local_storage = {} # this our database for today!

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET': #if a user gets the page, load it
        return render_template('home.html')
    else: # otherwise, promise the form input
        form = request.form
        user = form.get('user')
        password = form.get('password')
        check_user = False
        if user in local_storage and local_storage[user] == password:
            check_user = True # validate the login!
        if check_user:
            return render_template('logged_in.html', user=user)
        return render_template('home.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        form = request.form
        user = form.get('user')
        password = form.get('password')
        existing_user = False if user not in local_storage else True
        if existing_user: # make sure the user is unique!
            return render_template('signup.html')
        else:
            local_storage[user] = password
            return render_template('logged_in.html', user=user)

@app.route("/logged_in", methods=['GET'])
def logged_in():
    return render_template('logged_in.html')
