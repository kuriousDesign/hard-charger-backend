from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello, World! This is a Flask app.</h1>"


if __name__ == '__main__':
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.