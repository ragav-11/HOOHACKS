def run_scraper():
    import json
    import time

    sample_messages = [
        "You're so worthless, no one likes you.",
        "Just go disappear already.",
        "I can't sleep at all these days.",
        "Let's hang out this weekend!",
        "That was such a fun movie night!"
    ]

    output = []
    for msg in sample_messages:
        output.append({
            "user_id": "unknown",
            "username": "unknown",
            "platform": "MockPlatform",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "message_type": "text",
            "message": msg
        })

    with open("scraped_messages.json", "w") as f:
        json.dump(output, f, indent=4)
