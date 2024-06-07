from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_client_ip():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return render_template('index.html', client_ip=client_ip)

