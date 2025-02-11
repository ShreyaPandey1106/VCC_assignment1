from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/service1', methods=['GET'])
def service1():
    data = {"message": "Hello from Service 1"}
    service2_url = "http://192.168.56.2:5001/service2"  # VM2's internal IP
    response = requests.post(service2_url, json=data)
    return jsonify({"service1_response": "Sent to Service 2", "service2_response": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
