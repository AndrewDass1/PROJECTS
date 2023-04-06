from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

dictionary = {}

# HOME
@app.route("/")
def api_page():
    return render_template("choose_crud_command.html")

# POST
@app.route("/post_elements")
def post_page():
    return render_template("post_elements.html")

# PUT
@app.route("/put_elements")
def add_put_elements():
    global dictionary
    dictionary = {}
    return render_template("put_elements.html")

# DELETE
@app.route("/delete_page")
def the_delete_page():
    return render_template("delete_page.html")

@app.route("/delete_element", methods=['POST'])
def delete_element():
    key_value = request.form["entry1"]

    see_if_key_exists = dictionary.get(key_value)

    if see_if_key_exists == True:
        del dictionary[key_value]
        file = open("dictionary_file.pkl", 'wb')
        pickle.dump(dictionary, file)
        file.close()
        return render_template("delete_success.html")
    else:
        return render_template("error.html")

# Update Dictionary
@app.route("/success", methods=['POST'])
def success():
    html_data_1 = request.form["entry1"]
    html_data_2 = request.form["entry2"]

    dictionary[html_data_1] = html_data_2

    file = open("dictionary_file.pkl", 'wb')
    pickle.dump(dictionary, file)
    file.close()

    return render_template("success.html", html_data_1=html_data_1, html_data_2=html_data_2)

# GET
@app.route("/get_page")
def the_get_page():
    file = open('dictionary_file.pkl', 'rb')
    retrieve_dictionary = pickle.load(file)
    file.close()

    return render_template("get_page.html", retrieve_dictionary=retrieve_dictionary)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)


