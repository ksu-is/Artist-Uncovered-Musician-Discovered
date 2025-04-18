# Set up basic Flask app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    artist = request.form['artist']
    return render_template('results.html', artist=artist)

if __name__ == '__main__':
    app.run(debug=True)
