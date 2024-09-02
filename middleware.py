from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/productive_domains', methods=['GET'])
def productive_domains():
    productive_domains_list = ["www.atlassian.com", "www.udemy.com", "stackoverflow.com"]
    return jsonify(productive_domains_list)

@app.route('/productive_apps', methods=['GET'])
def productive_apps():
    productive_apps_list = {
        "Code.exe": "Visual Studio Code",
        "WINWORD.EXE": "Microsoft Word",
        "POWERPNT.EXE": "Microsoft PowerPoint",
        "EXCEL.EXE": "Microsoft Excel",
        "chrome.exe": "Google Chrome",
        "notepad++.exe": "Notepad++",
        "photoshop.exe": "Adobe Photoshop",
        "illustrator.exe": "Adobe Illustrator"
    }
    return jsonify(productive_apps_list)

@app.route('/leisure_domains', methods=['GET'])
def leisure_domains():
    leisure_domains_list = ["www.facebook.com", "www.youtube.com", "www.instagram.com"]
    return jsonify(leisure_domains_list)

# Dirección IP del servidor local al que te quieres conectar
SERVER_URL = "http://192.168.100.10"

@app.route('/player/<username>/<password>', methods=['GET'])
def player_login(username, password):
    try:
        url = f"{SERVER_URL}:3010/player/{username}/{password}"
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Connection failed: {str(e)}"}), 500

@app.route('/player_all_attributes/<user_id>', methods=['GET'])
def get_player_attributes(user_id):
    try:
        response = requests.get(f'{SERVER_URL}:3001/player_all_attributes/{user_id}')
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/spend_attribute/', methods=['POST'])
def spend_attribute():
    try:
        data = request.json
        response = requests.post(f'{SERVER_URL}:3002/spend_attribute/', json=data)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ejecutar en modo de desarrollo no es recomendable para producción
    app.run(port=5001)