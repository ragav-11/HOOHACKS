import smtplib
import json
import os

# Load user data
def load_users():
    user_file = "analyzed_messages.json"
    if not os.path.exists(user_file):
        print("❌ Failed to load local user file: registered_users.json not found.")
        return []
    
    with open(user_file, "r") as f:
        try:
            users = json.load(f)
            print(f"✅ Successfully loaded {len(users)} registered users.")
            return users
        except json.JSONDecodeError:
            print("❌ Error: Failed to parse JSON in registered_users.json.")
            return []

# Function to send email alerts
def send_alerts(flagged_messages):
    if not flagged_messages:
        print("✅ No flagged messages to process.")
        return
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_app_password"  # Replace with an app password (not your actual password)
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
    except smtplib.SMTPAuthenticationError:
        print("❌ SMTP Authentication Error: Check your email credentials and security settings.")
        return
    except Exception as e:
        print(f"❌ Error: Could not connect to SMTP server: {e}")
        return

    print(f"🚨 {len(flagged_messages)} flagged messages found. Notifying users...")

    for message in flagged_messages:
        to_email = "recipient@example.com"  # Replace with actual recipient logic
        subject = "🚨 Digital Watchdog Alert: Flagged Message Detected"
        body = f"User: {message['username']}\nMessage: {message['message']}\nPlatform: {message['platform']}\nConfidence Score: {message['confidence_score']}"
        email_text = f"Subject: {subject}\n\n{body}"

        try:
            server.sendmail(sender_email, to_email, email_text)
            print(f"✅ Email successfully sent to {to_email} for message: {message['message']}")
        except smtplib.SMTPException as e:
            print(f"❌ Failed to send email to {to_email}: {e}")

    server.quit()

# Example flagged messages for testing
flagged_messages = [
    {"username": "unknown", "message": "You're so worthless, no one likes you.", "platform": "MockPlatform", "confidence_score": 0.9783},
    {"username": "unknown", "message": "Just go disappear already.", "platform": "MockPlatform", "confidence_score": 0.5973},
]

# Execute
users = load_users()
send_alerts(flagged_messages)