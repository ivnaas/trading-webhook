import json, config
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello, World!!'

@app.route('/webhook', methods=['POST'])
def webhook():
   # print(request.data)
    data = json.loads(request.data)
    if data['auth-token'] != config.WEBHOOK_AUTHTOKEN:
        return {
            "code": "error",
            "message": "invalid auth-token"
        }
    print(data['value3'])
    return {
        "code": "success",
        "message": data
    }

