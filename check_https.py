from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    protocol = None
    url = None

    if request.method == 'POST':
        url = request.form['url']
        if url:
            if url.startswith('http://'):
                protocol = 'HTTP'
            elif url.startswith('https://'):
                protocol = 'HTTPS'
            else:
                # Default to assume HTTP if no prefix is given
                protocol = 'HTTP (assumed)'
                
            # Optionally, check the actual response
            try:
                response = requests.get(url, timeout=5)
                if response.url.startswith('https://'):
                    protocol = 'HTTPS (Confirmed)'
                else:
                    protocol = 'HTTP (Confirmed)'
            except requests.RequestException:
                protocol = 'Invalid URL or unresponsive website'

    return render_template('index.html', protocol=protocol, url=url)

if __name__ == '__main__':
    app.run(debug=True)