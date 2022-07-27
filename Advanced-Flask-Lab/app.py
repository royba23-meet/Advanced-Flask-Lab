from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "static/images/avatar.gif"

user_bio = "Monkey goes brrrrr"



posts = {
    "static/images/taxi.png": "Taxi monkey my beloved",
    "static/images/avatar.gif": "Average middle eastern",
    "static/images/monke.png": "Normal day at Australia",
}

#####


@app.route('/')  # '/' for the default page
def home():
    return render_template(
        'index.html',
        bio=user_bio,
        image=image_link,
        posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
