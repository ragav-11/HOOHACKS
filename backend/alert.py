import json
import smtplib
from email.mime.text import MIMEText
from firebase import FirebaseAuth

class AlertSystem:
    def __init__(self, analyzed_messages_file="analyzed_messages.json", user_file="registered_users.json"):
        self.analyzed_messages_file = analyzed_messages_file
        self.firebase_auth = FirebaseAuth(user_file)  # Load registered users
        self.users = self.firebase_auth.get_registered_users  # Get the list of emails

    """Filter messages that are classified as Harmful or Needs Attention."""
    def send_alert(self, recipient_email, flagged_messages):
        """Simulated alert sending via email (replace with actual email sending)."""
        if not flagged_messages:
            return

        subject = "Alert: Potential Harmful Messages Detected"
        body = "The following messages have been flagged:\n\n"
        for msg in flagged_messages:
            body += f"- {msg['message']} (Classification: {msg['classification']}, Confidence: {msg['confidence_score']:.2f})\n"

        # Format email
        email_msg = MIMEText(body)
        email_msg["Subject"] = subject
        email_msg["From"] = "ragav@vt.edu"  # Replace with your sender email
        email_msg["To"] = recipient_email

        # Simulated sending (replace with real SMTP configuration)
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:  
                server.starttls()
                server.login("ragavmj23@gmail.com", "RagavRajan123")  
                server.sendmail("ragavmj23@gmail.com", recipient_email, email_msg.as_string())

            print(f"Alert sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")

    def notify_users(self, flagged_messages):
        """Send alerts to all registered users if flagged messages are detected."""
        if not flagged_messages:
            print("No harmful messages detected. No alerts needed.")
            return

        for user_email in self.users:
            self.send_alert(user_email, flagged_messages)