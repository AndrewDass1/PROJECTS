from flask import Flask
import random

application = Flask(__name__)
app = application

@application.route("/")
def rand_number():
    random_number = str(random.randint(1, 100))
    return "The random number is " + random_number

if __name__== '__main__':
    application.run(host="0.0.0.0", debug=True, port=5000)
