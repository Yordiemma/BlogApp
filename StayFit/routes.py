from flask import render_template
from . import app  # Import the Flask app instance

@app.route('/')
def home():
    return render_template('index.html')  # Render the 'index.html' template for the home page

@app.route('/posts')
def posts():
    # Dummy data for example
    posts = ["Post 1", "Post 2", "Post 3"]  # Example data for posts
    return render_template('posts.html', posts=posts)  # Pass posts data to the 'posts.html' template

@app.route('/about')
def about():
    return render_template('about.html')  # Render the 'about.html' template for the about page
