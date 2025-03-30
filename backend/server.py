from flask import Flask, jsonify, request
from flask_cors import CORS
from webscraper import run_scraper
from text_analysis import message_analysis
from alert import send_alerts

app = Flask(__name__)
CORS(app)

@app.route("/run-detection", methods=["POST"])
def run_detection():
    run_scraper()
    classified = message_analysis("scraped_messages.json")
    alerts = send_alerts(classified)
    return jsonify({"alerts": alerts})

@app.route("/analyze_messages", methods=["POST"])
def analyze_messages():
    data = request.json  # Expecting JSON input
    if not data or "messages" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    classified = message_analysis(data["messages"])
    return jsonify({"classified_messages": classified})

if __name__ == "__main__":
    app.run(port=5000)