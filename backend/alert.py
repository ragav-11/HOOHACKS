import smtplib
import json
import os
from email.mime.text import MIMEText

class AlertSystem:
    def __init__(self, analyzed_messages_file="analyzed_messages.json", user_file="registered_users.json"):
        self.analyzed_messages_file = analyzed_messages_file
        self.user_file = user_file
        self.users = self.load_users()
        print(f"✅ Successfully loaded {len(self.users)} registered users.")

    def load_users(self):
        """Load registered users from a JSON file."""
        if not os.path.exists(self.user_file):
            print(f"❌ Error: User file {self.user_file} not found.")
            return []
        try:
            with open(self.user_file, "r") as f:
                users = json.load(f)
            return users
        except json.JSONDecodeError:
            print("❌ Error: Failed to parse JSON in the user file.")
            return []

    def send_email(self, to_email, subject, body):
        """Send an email notification using Gmail's SMTP."""
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@gmail.com"       # Replace with your Gmail address
        sender_password = "your_app_password"         # Replace with your generated App Password

        email_msg = MIMEText(body)
        email_msg["Subject"] = subject
        email_msg["From"] = sender_email
        email_msg["To"] = to_email

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, to_email, email_msg.as_string())
            print(f"✅ Email successfully sent to {to_email}")
        except smtplib.SMTPAuthenticationError:
            print("❌ SMTP Authentication Error: Check your email credentials and security settings.")
        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {e}")

    def notify_users(self, flagged_messages):
        """Notify all registered users if flagged messages are detected."""
        if not flagged_messages:
            print("✅ No harmful messages detected. No alerts needed.")
            return

        print(f"🚨 {len(flagged_messages)} flagged messages found. Notifying users...")

        subject = "🚨 Digital Watchdog Alert: Flagged Message Detected"
        body = "The following messages have been flagged:\n\n"
        for msg in flagged_messages:
            body += f"- {msg['message']} (Classification: {msg['classification']}, Confidence: {msg['confidence_score']:.2f})\n"

        # Notify each user, only if the user object contains an "email" key.
        for user in self.users:
            if "email" in user:
                self.send_email(user["email"], subject, body)
            else:
                print(f"❌ User entry {user} does not have an 'email' key.")

# Testing the Alert System if running alert.py directly
if __name__ == "__main__":
    alert_system = AlertSystem()
    # Example flagged messages for testing:
    test_flagged_messages = [
        {"username": "unknown", "message": "You're so worthless, no one likes you.", "platform": "MockPlatform", "classification": "Needs Attention", "confidence_score": 0.9783},
        {"username": "unknown", "message": "Just go disappear already.", "platform": "MockPlatform", "classification": "Needs Attention", "confidence_score": 0.5973}
    ]
    alert_system.notify_users(test_flagged_messages)