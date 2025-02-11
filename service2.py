from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/service2', methods=['POST'])
def service2():
    data = request.json
    return jsonify({"received": data, "response": "Hello from Service 2"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
