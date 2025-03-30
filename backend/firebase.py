import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

class FirebaseAuth:
    def __init__(self, user_file="analyzed_messages.json"):
        self.user_file = user_file
        self.db = None

        # Try to initialize Firebase with service account
        if os.path.exists("firebase_credentials.json"):
            try:
                cred = credentials.Certificate("firebase_credentials.json")
                firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                print("✅ Firebase initialized successfully.")
            except Exception as e:
                print(f"⚠️ Failed to initialize Firebase: {e}")
        else:
            print("⚠️ firebase_credentials.json not found. Falling back to local user file.")

    def get_registered_users(self):
        """Fetch registered user emails from Firestore or local file."""
        if self.db:
            try:
                users_ref = self.db.collection("users")
                docs = users_ref.stream()
                emails = []

                for doc in docs:
                    data = doc.to_dict()
                    email = data.get("email")
                    if email:
                        emails.append(email)

                print(f"✅ Retrieved {len(emails)} user(s) from Firestore.")
                return emails
            except Exception as e:
                print(f"⚠️ Error reading from Firestore: {e}")

        # Fallback: read from local file
        try:
            with open(self.user_file, "r") as f:
                data = json.load(f)
                return data.get("emails", []) if isinstance(data, dict) else data
        except Exception as e:
            print(f"❌ Failed to load local user file: {e}")
            return []