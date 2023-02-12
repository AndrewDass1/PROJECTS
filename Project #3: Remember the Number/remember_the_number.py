from flask import Flask, render_template
import the_code

app = Flask(__name__)

@app.route("/")
def firstpage():
    return render_template('firstpage.html')

@app.route("/how_many_digits")
def secondpage():
    return render_template('')

@app.route("/the_number")
def thirdpage():
    return render_template('')

@app.route("/enter_the_number")
def fourthpage():
    return render_template('')

@app.route("/final_results")
def fifthpage():
    return render_template('')

  
if __name__== '__main__':
  app.run(host="0.0.0.0", debug=True, port=5000)
