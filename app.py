
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/Bahram')
def your_name():
    return 'This is my page'

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get("name", "")
    if name:
        return f"Hello {name}"
    else:
        return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
