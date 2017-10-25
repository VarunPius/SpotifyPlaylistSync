from app import app
from flask import render_template


items = [{"id":0, "name": "First item"}, {"id":2, "name": "third item"}]

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'test'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html', user = user, posts = posts, title = "Home")

def search() -> list:
    return items