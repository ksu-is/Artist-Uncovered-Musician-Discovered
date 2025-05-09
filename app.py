from flask import Flask, render_template, request
from spotify_basic import search_artist

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    artist_name = request.form['artist']
    result = search_artist(artist_name)
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
