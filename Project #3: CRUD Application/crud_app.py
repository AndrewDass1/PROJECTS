from flask import Flask, render_template, request
import pickle, time, os
from flask_apscheduler import APScheduler

app = Flask(__name__)

global dictionary
dictionary = {}
file = open("dictionary_file.pkl", 'wb')
pickle.dump(dictionary, file)
file.close()

execute_clear_dictionary = APScheduler()

@app.route("/")
def crud_page():
    return render_template("/choose_crud_command.html")

# POST
@app.route("/post_elements")
def post_page():
    return render_template("/post_elements.html")

# PUT
@app.route("/put_elements")
def add_put_elements():
    dictionary = {}
    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()
    return render_template("/put_elements.html")

# Update Dictionary
@app.route("/success", methods=['POST'])
def success():
    file = open("dictionary_file.pkl", 'rb')
    dictionary = pickle.load(file)
    file.close()

    html_data_1 = request.form["entry1"]
    html_data_2 = request.form["entry2"]
    dictionary[html_data_1] = html_data_2

    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()
    time.sleep(1)

    return render_template("/success.html", html_data_1=html_data_1, html_data_2=html_data_2)

# GET
@app.route("/get_page")
def the_get_page():
    file = open('dictionary_file.pkl', 'rb')
    retrieve_dictionary = pickle.load(file)
    file.close()
    return render_template("/get_page.html", retrieve_dictionary=retrieve_dictionary)


# DELETE
@app.route("/delete_page")
def the_delete_page():
    file = open('dictionary_file.pkl', 'rb')
    retrieve_dictionary = pickle.load(file)
    file.close()

    return render_template("/delete_page.html", retrieve_dictionary=retrieve_dictionary)

@app.route("/delete_element", methods=['POST'])
def delete_element():
    file = open('dictionary_file.pkl', 'rb')
    dictionary = pickle.load(file)
    file.close()
    key = request.form["entry1"]    

    if key in dictionary.keys():
        del dictionary[key]
        file = open("dictionary_file.pkl", 'wb')
        pickle.dump(dictionary, file)
        file.close()
        time.sleep(1)
        return render_template("/delete_success.html")
    else:
        return render_template("/error.html")

def clear_dictionary():
    os.remove("dictionary_file.pkl")
    dictionary = {}
    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()

if __name__== '__main__':
    execute_clear_dictionary.add_job(id = 'Scheduled Task', func=clear_dictionary, trigger="interval", seconds=300)
    execute_clear_dictionary.start()
    app.run(host="0.0.0.0", debug=True, port=5000)


