from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def get_client_ip():
    try:
        # Get the X-Forwarded-For header value, or fall back to remote_addr if not present
        x_forwarded_for = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        # Split the X-Forwarded-For header into a list of IPs
        ip_list = x_forwarded_for.split(',')
        
        # Strip whitespace from each IP address
        ip_list = [ip.strip() for ip in ip_list]
        
        app.logger.debug(f"Client IPs: {ip_list}")
        return render_template('index.html', ip_list=ip_list)
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return "An error occurred", 500

