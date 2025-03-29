from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cyberbullying_db"]  # Create or access database
flagged_messages = db["flagged_messages"]  # Collection for flagged content
alert_logs = db["alert_logs"]  # Collection for alert logs
