import firebase_admin
from firebase_admin import credentials, auth
import json
import os

# Load Firebase credentials (replace 'firebase_key.json' with your actual key file)
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

class FirebaseAuth:
    def __init__(self, user_file="registered_users.json"):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        """Load user emails from JSON file (if exists)."""
        if os.path.exists(self.user_file):
            with open(self.user_file, "r") as file:
                return json.load(file)
        return []

    def save_users(self):
        """Save user emails to JSON file."""
        with open(self.user_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def register_user(self, email, password):
        """Register a new user and store email for alerts."""
        try:
            user = auth.create_user(email=email, password=password)
            print(f"User {email} registered successfully!")

            # Store email for notifications
            if email not in self.users:
                self.users.append(email)
                self.save_users()

            return user.uid
        except Exception as e:
            print(f"Error registering user: {e}")
            return None

    def login_user(self, email, password):
        """Simulate login by checking Firebase auth (since Firebase Admin SDK doesn’t verify passwords)."""
        if email in self.users:
            print(f"User {email} logged in successfully!")
            return True
        print("Login failed: User not found.")
        return False
    
    """Creates a dictionary of every users emails"""
    def get_registered_users(self):
        return list(self.users.keys())

# Example usage:
if __name__ == "__main__":
    firebase_auth = FirebaseAuth()

    #
    users_to_register = []

    for email, password in users_to_register:
        firebase_auth.register_user(email, password)


    # Login user
    firebase_auth.login_user("parent@example.com", "securepassword")