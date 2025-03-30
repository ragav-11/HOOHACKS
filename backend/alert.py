import json
import smtplib
import os
from email.mime.text import MIMEText
from firebase import FirebaseAuth  # Assumes you have this class implemented
from dotenv import load_dotenv

# Load environment variables (email, password)
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

class AlertSystem:
    def __init__(self, analyzed_messages_file="analyzed_messages.json", user_file="analyzed_messages.json"):
        self.analyzed_messages_file = analyzed_messages_file
        self.firebase_auth = FirebaseAuth(user_file)
        self.users = self.firebase_auth.get_registered_users()

def send_alerts(analyzed_messages_path="analyzed_messages.json"):
    from firebase import FirebaseAuth
    import smtplib
    from email.mime.text import MIMEText

    auth = FirebaseAuth()
    users = auth.get_registered_users()

    with open(analyzed_messages_path, "r") as f:
        messages = json.load(f)

    flagged = [m for m in messages if m["classification"] in ["Harmful", "Needs Attention"]]

    if not flagged:
        return []

    for user in users:
        body = "\n".join(
            f"- {m['message']} ({m['classification']}, {m['confidence_score']:.2f})"
            for m in flagged
        )
        msg = MIMEText(body)
        msg["Subject"] = "🚨 Cyberbullying Alert"
        msg["From"] = "noreply@yourapp.com"
        msg["To"] = user

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login("your_email@gmail.com", "your_app_password")
                server.send_message(msg)
        except Exception as e:
            print(f"Failed to send email to {user}: {e}")

    return flagged

# Run example
if __name__ == "__main__":
    alert_system = AlertSystem()
    alert_system.notify_users()