from flask import Flask, jsonify
from webscraper import run_scraper
from text_analysis import message_analysis
from alert import send_alerts

app = Flask(__name__)

@app.route("/run-detection", methods=["POST"])
def run_detection():
    run_scraper()
    classified = message_analysis()
    alerts = send_alerts()
    return jsonify({"alerts": alerts})

if __name__ == "__main__":
    app.run(port=5000)