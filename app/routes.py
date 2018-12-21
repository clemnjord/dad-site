from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Alain Puech")

@app.route('/images')
def images():
    #return 'images'
    return render_template('oeuvres.html')

@app.route('/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('oeuvres.html', image=post_id)
