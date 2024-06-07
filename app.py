from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')
    except requests.RequestException:
        return 'Unable to retrieve IP address'

@app.route('/')
def get_node_name():
    public_ip = get_public_ip()
    return render_template('index.html', node_name=public_ip)
