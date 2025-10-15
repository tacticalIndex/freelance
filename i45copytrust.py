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
    
    if authorization == process.env.accountjoinheader and serverid is not None:
        pyautogui.click(x=0, y=0) # Placeholder, servers tab
        pyautogui.click(x=0, y=0) # Placeholder, search bar
        pyautogui.write(serverid) 
        pyautogui.press('enter')
        pyautogui.click(x=0, y=0) # Placeholder, whatever team (who knows what)
        pyautogui.click(x=0, y=0) # Placeholder, spawn on selected team

        
        payload = {
            "readyForExecution": True,
            "message": "i55 ready for service 👽"
        }
        return jsonify(payload), 200
    elif serverid is None:
        payload = {
            "readyForExecution": False,
            "message": "i55 not ready for service 🥀",
            "errorMessage": "Argument: `serverid` was missing from the request."
        }
        return jsonify(payload), 400
    elif authorization != process.env.accountjoinheader:
        payload = {
            "readyForExecution": False,
            "message": "i55 not ready for service 🥀",
            "errorMessage": "Authorization header is not valid.
        }
        return jsonify(payload), 400
