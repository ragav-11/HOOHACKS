import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


"""Function that tries multiple selectors"""
def get_elements_by_candidates(driver, method, candidate_selectors, max_wait=10):
    elements = []
    for candidate in candidate_selectors:
        start_time = time.time()
        while time.time() - start_time < max_wait:
            try:
                if method == "xpath":
                    elements = driver.find_elements(By.XPATH, candidate)
                else:  # assume CSS
                    elements = driver.find_elements(By.CSS_SELECTOR, candidate)
                if elements and len(elements) > 0:
                    return elements
            except Exception as e:
                # If an error occurs (e.g., invalid selector), try the next candidate
                break
            time.sleep(1)
    return elements
# Setup Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# JSON File Path
json_file_path = "scraped_messages.json"

# Function to save messages in JSON format
def save_messages(messages):
    try:
        # Read existing data if file exists
        try:
            with open(json_file_path, "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append new messages
        existing_data.extend(messages)

        # Save back to JSON file
        with open(json_file_path, "w") as f:
            json.dump(existing_data, f, indent=4)

        print(f"Saved {len(messages)} new messages.")
    except Exception as e:
        print("Error saving messages:", e)

# **1. Scraper for Instagram Messages**
def scrape_instagram():
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(10)

    # Candidate selectors for Instagram messages (XPath in this example)
    candidate_selectors = [
        '//div[@role="presentation"]//div[contains(@class, "x1lliihq")]',
        '//div[contains(@class, "message-text")]',
        '//div[@aria-label="Message"]'
    ]
    
    message_elements = get_elements_by_candidates(driver, method="xpath", candidate_selectors=candidate_selectors, max_wait=10)
    messages = []
    seen_texts = set()  # To avoid duplicates
    for element in message_elements:
        message_text = element.text.strip()
        if message_text and message_text not in seen_texts:
            messages.append({
                "user_id": "unknown",
                "username": "unknown",
                "platform": "Instagram",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "message_type": "text",
                "message": message_text
            })
            seen_texts.add(message_text)

    save_messages(messages)

# **2. Scraper for WhatsApp Web Messages**
def scrape_whatsapp():
    driver.get("https://web.whatsapp.com/")
    input("Press Enter...")  # Requires manual login
    time.sleep(5)

    # Candidate selectors for WhatsApp messages (CSS selectors)
    candidate_selectors = [
        "span.selectable-text",
        "div.message-text"
    ]
    message_elements = get_elements_by_candidates(driver, method="css", candidate_selectors=candidate_selectors, max_wait=10)  # Update selector

    messages = []
    for element in message_elements:
        message_text = element.text.strip()
        if message_text:
            messages.append({
                "user_id": "unknown",
                "username": "unknown",
                "platform": "WhatsApp",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "message_type": "text",
                "message": message_text
            })

    save_messages(messages)

# **3. Scraper for Telegram Web**
def scrape_telegram():
    driver.get("https://web.telegram.org/")
    time.sleep(5)

    # Candidate selectors for Telegram messages (CSS selectors)
    candidate_selectors = [
        "div.message",
        "div.chat-message"
    ]
    message_elements = get_elements_by_candidates(driver, method="css", candidate_selectors=candidate_selectors, max_wait=10)

    messages = []
    for element in message_elements:
        message_text = element.text.strip()
        if message_text:
            messages.append({
                "user_id": "unknown",
                "username": "unknown",
                "platform": "Telegram",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "message_type": "text",
                "message": message_text
            })

    save_messages(messages)

# **4. Scraper for Discord**
def scrape_discord():
    driver.get("https://discord.com/channels/@me")
    input("Log in manually and press Enter...")  # Requires manual login
    time.sleep(5)
    
    # Candidate selectors for Discord messages (CSS selectors)
    candidate_selectors = [
        "div.markup",
        "div.messageContent-2t3eCI"
    ]
    message_elements = get_elements_by_candidates(driver, method="css", candidate_selectors=candidate_selectors, max_wait=10)

    messages = []

    for element in message_elements:
        message_text = element.text.strip()
        if message_text:
            messages.append({
                "user_id": "unknown",
                "username": "unknown",
                "platform": "Discord",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "message_type": "text",
                "message": message_text
            })

    save_messages(messages)

# **Main Function to Select Platforms**
def scrape_all_sites():
    sites = {
        "instagram": scrape_instagram,
        "whatsapp": scrape_whatsapp,
        "telegram": scrape_telegram,
        "discord": scrape_discord
    }

    print("Available sites:", ", ".join(sites.keys()))
    choice = input("Enter site to scrape (or 'all' for everything): ").lower()

    if choice == "all":
        for site, function in sites.items():
            print(f"Scraping {site}...")
            function()
    elif choice in sites:
        print(f"Scraping {choice}...")
        sites[choice]()
    else:
        print("Invalid choice!")

# **Run the Scraper**
if __name__ == "__main__":
    scrape_all_sites()
    driver.quit()
