from flask import Flask, request, jsonify
import pyautogui

app = Flask(__name__)

@app.route('/accountjoin', methods=['POST'])
def account_join():
    serverid = request.args.get("serverid")
    headers = request.headers
    authorization = headers.get('Authorization')

    if authorization is None:
        return "Authorization Header is not found.", 401
    
    if authorization == process.env.accountjoinheader:
        try: 
            