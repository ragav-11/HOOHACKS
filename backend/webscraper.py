from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Setup Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("user-data-dir=./chrome_session")  # Use this for persistent login
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_telegram():
    driver.get("https://web.telegram.org/")
    print("Waiting for Telegram Web to load...")
    time.sleep(5)  # Allow time for Telegram Web to load (you can consider improving this with dynamic waits)

    try:
        # Wait for the conversation list to load dynamically
        chat_area = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="chat-list"]'))
        )
        print("Telegram chat area loaded.")
    except Exception as e:
        print(f"Error loading Telegram chat area: {e}")
        return

    messages = []

    # Ensure the message elements are available dynamically
    message_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "message--content")]//div[contains(@class, "markup")]')

    print(f"Found {len(message_elements)} messages.")
    
    if message_elements:
        for element in message_elements:
            message_text = element.text.strip()
            if message_text:
                messages.append({
                    "user_id": "unknown",  # Optionally, capture user IDs dynamically if required
                    "username": "unknown",  # Capture usernames dynamically if available
                    "platform": "Telegram",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "message_type": "text",
                    "message": message_text
                })

    # Send scraped messages to the backend server for classification and further processing
    if messages:
        send_messages_to_backend(messages)
    else:
        print("No messages to send to the backend.")

    # Close the driver after scraping
    driver.quit()

def send_messages_to_backend(messages):
    """Send the scraped messages to the backend server for analysis."""
    backend_url = "http://localhost:5000/analyze_messages"  # Change to your backend server's URL

    try:
        response = requests.post(backend_url, json={"messages": messages})
        if response.status_code == 200:
            print("Messages sent to backend for analysis.")
        else:
            print(f"Failed to send messages to backend. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending messages to backend: {e}")

# Call the function to scrape and send data to the backend
scrape_telegram()