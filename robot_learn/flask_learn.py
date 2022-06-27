from flask import Flask
import markupsafe
from markupsafe import escape
from flask import render_template
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/me")
def me_api():
    a= {
        "username": "sd",
        "theme": "er"
    }
    return jsonify(a)
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World1'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hello, World1post'
    else:
        return 'Hello, World1get'

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'