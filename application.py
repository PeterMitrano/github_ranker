from flask import Flask, render_template, request
import requests

api = 'https://api.github.com/'
userURL = api + 'users/'

# EB looks for an 'app' callable by default.
app = Flask(__name__)

@app.route('/')
def get_root():
    return render_template('index.html')

@app.route('/rank')
def get_predict():
    user = request.args.get('user')
    rank = calculate_rank(user)
    return render_template('rank.html',
            rank=rank)

def calculate_rank(user):
    url = userURL + user
    request = requests.get(url)
    repo = request.json()
    commits = request.json()
    return repo['public_repos']


# run the app.
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.run(debug = True)

