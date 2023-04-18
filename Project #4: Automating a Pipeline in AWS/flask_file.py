from flask import Flask

app = Flask(__name__)

@app.route("/")
def run_hello_world():
    return "The flask application ran successfully!"

if __name__== '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)