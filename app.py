import os
from flask import Flask, render_template

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    """Homepage showcasing Moje Streaming app"""
    return render_template('index.html')

@app.route('/moje-streaming-csae-policy')
def csae_policy():
    """CSAE Policy page"""
    return render_template('csae-policy.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Privacy Policy page"""
    return render_template('privacy-policy.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
