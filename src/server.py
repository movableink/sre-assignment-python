from flask import Flask, jsonify
from requests.exceptions import RequestException
from .config import Config
from .geoip import lookup_ip

app = Flask(__name__)

@app.route('/lookup/<ip>')
def get_ip_info(ip):
    try:
        result = lookup_ip(ip)
        return jsonify(result)
    except RequestException as e:
        error_message = f"API request failed: {e}"
        return jsonify({"error": error_message}), 500

def main():
    app.run(port=Config.PORT)
