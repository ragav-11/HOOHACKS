import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome WebDriver
chrome_options = Options()
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
    chrome_options.add_argument("user-data-dir=./insta_session")
    driver.get("https://www.instagram.com/direct/inbox/")
    time.sleep(100)

    for i in range(10):
        message_elements = driver.find_elements(By.XPATH, '//div[@role="presentation"]//div[contains(@class, "x1lliihq")]')
        if len(message_elements) > 0:
            break
        time.sleep(1)
    messages = []

    for element in message_elements:
        message_text = element.text.strip()
        if message_text:
            messages.append({
                "user_id": "unknown",
                "username": "unknown",
                "platform": "Instagram",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "message_type": "text",
                "message": message_text
            })

    save_messages(messages)

# **2. Scraper for WhatsApp Web Messages**
def scrape_whatsapp():
    print("Opening WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    input("Scan QR code in the opened browser, press Enter when your chats load...")

    chat_name = input("Enter the exact name of the chat (case sensitive): ")
    time.sleep(2)

    # Click the chat using search
    try:
        search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    except:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(chat_name)
    time.sleep(2)

    chat = driver.find_element(By.XPATH, f'//span[@title="{chat_name}"]')
    chat.click()
    time.sleep(3)

    # Scroll to load older messages
    for _ in range(3):
        driver.execute_script("document.querySelector('[aria-label=\"Message list\"]').scrollTop = 0")
        time.sleep(1)

    # Extract message text
    message_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "_21Ahp") or contains(@class, "_1Gy50")]//span[@class="selectable-text copyable-text"]')

    print(f"Found {len(message_elements)} messages.")
    messages = []
    for element in message_elements:
        message_text = element.text.strip()
        if message_text:
            print("Scraped:", message_text)
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

    messages = []
    message_elements = driver.find_elements(By.CLASS_NAME, "message")  # Update selector

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

    messages = []
    message_elements = driver.find_elements(By.CSS_SELECTOR, "div.markup")  # Update selector

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
