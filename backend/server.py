from flask import Flask, jsonify
from webscraper import run_scraper
from text_analysis import message_analysis
from alert import AlertSystem  # Import the class AlertSystem

app = Flask(__name__)

@app.route("/run-detection", methods=["POST"])
def run_detection():
    # 1. Run the scraper to create or update analyzed_messages.json
    run_scraper()  

    # 2. Run text analysis on the scraped messages
    classified_messages = message_analysis()  # Ensure this returns the classified messages

    # 3. Use AlertSystem to notify users
    alert_system = AlertSystem()
    alert_system.notify_users(classified_messages)

    return jsonify({"status": "Detection and alerts processed."})

if __name__ == "__main__":
    app.run(port=5000, debug=True)