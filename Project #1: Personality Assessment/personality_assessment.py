from flask import Flask, render_template
import questions

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("welcome_page.html")

@app.route("/assessment")
def start_assessment():
    question1, q1_answer1, q1_answer2, q1_answer3, q1_answer4, question2, q2_answer1, q2_answer2, q2_answer3, q2_answer4, question3, q3_answer1, q3_answer2, q3_answer3, q3_answer4, question4, q4_answer1, q4_answer2, q4_answer3, q4_answer4, question5, q5_answer1, q5_answer2, q5_answer3, q5_answer4, question6, q6_answer1, q6_answer2, q6_answer3, q6_answer4, question7, q7_answer1, q7_answer2, q7_answer3, q7_answer4, question8, q8_answer1, q8_answer2, q8_answer3, q8_answer4, question9, q9_answer1, q9_answer2, q9_answer3, q9_answer4, question10, q10_answer1, q10_answer2, q10_answer3, q10_answer4 = questions.the_test()
    return render_template("begin_assessment.html", question1=question1, q1_answer1=q1_answer1, q1_answer2=q1_answer2, q1_answer3=q1_answer3, q1_answer4=q1_answer4, question2=question2, q2_answer1=q2_answer1, q2_answer2=q2_answer2, q2_answer3=q2_answer3, q2_answer4=q2_answer4, question3=question3, q3_answer1=q3_answer1, q3_answer2=q3_answer2, q3_answer3=q3_answer3, q3_answer4=q3_answer4, question4=question4, q4_answer1=q4_answer1, q4_answer2=q4_answer2, q4_answer3=q4_answer3, q4_answer4=q4_answer4, question5=question5, q5_answer1=q5_answer1, q5_answer2=q5_answer2, q5_answer3=q5_answer3, q5_answer4=q5_answer4, question6=question6, q6_answer1=q6_answer1, q6_answer2=q6_answer2, q6_answer3=q6_answer3, q6_answer4=q6_answer4, question7=question7, q7_answer1=q7_answer1, q7_answer2=q7_answer2, q7_answer3=q7_answer3, q7_answer4=q7_answer4, question8=question8, q8_answer1=q8_answer1, q8_answer2=q8_answer2, q8_answer3=q8_answer3, q8_answer4=q8_answer4, question9=question9, q9_answer1=q9_answer1, q9_answer2=q9_answer2, q9_answer3=q9_answer3, q9_answer4=q9_answer4, question10=question10, q10_answer1=q10_answer1, q10_answer2=q10_answer2, q10_answer3=q10_answer3, q10_answer4=q10_answer4)

@app.route("/sad")
def sad():
    return render_template("sad.html")

@app.route("/angry")
def angry():
    return render_template("angry.html")

@app.route("/neutral")
def neutral():
    return render_template("neutral.html")

@app.route("/elated")
def elated():
    return render_template("elated.html")

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)