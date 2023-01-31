from flask import Flask, render_template
import randomized_pokemon

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/pokemon_result.html")    
def the_pokemon_result():
    url_link, random_pokemon_image, pokemon_name = randomized_pokemon.chosen_pokemon()
    return render_template('pokemon_result.html', url_link=url_link, random_pokemon_image=random_pokemon_image, pokemon_name=pokemon_name)



if __name__== '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)