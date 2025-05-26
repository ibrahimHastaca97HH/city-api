# main.py
from flask import Flask, jsonify
from il_ilce_updater import fetch_and_save_iller_ilceler
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API çalışıyor."})

@app.route("/update")
def update():
    result = fetch_and_save_iller_ilceler()
    return jsonify(result)

@app.route("/data")
def data():
    try:
        with open("iller_ilceler.json", "r", encoding="utf-8") as f:
            content = f.read()
        return app.response_class(content, mimetype='application/json')
    except FileNotFoundError:
        return jsonify({"error": "Veri henüz oluşturulmadı"}), 404
