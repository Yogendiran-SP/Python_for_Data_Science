# For launching and controlling Chrome
from selenium import webdriver

# To help us locate elements by XPATH, name, etc
from selenium.webdriver.common.by import By

# To configure and launch the ChromeDriver properly
from selenium.webdriver.chrome.service import Service

# So we can pause the script when needed (for QR scan, element load, etc.).
import time

driver_path="C:\Program Files\Google\Chrome\Application\chrome.exe" # This sets the path to your chromedriver.exe

service = Service(driver_path)   # Sets up a Service object with your ChromeDriver

options = webdriver.ChromeOptions()   # ChromeOptions() allows us to customize the browser.
options.add_argument("--user-data-dir=whatsapp_profile")  # Creates a new Chrome profile folder called whatsapp_profile, It remembers your QR login, so you don’t have to scan the code again next time.

# This launches Chrome using the path to the driver and the custom options, Now you have full browser control through the driver object.
driver = webdriver.Chrome(service=service, options=options)

# Opens the WhatsApp Web page, The user must scan the QR code manually if it’s the first time.
driver.get("https://web.whatsapp.com")

# Gives you 15 seconds to scan the QR code.
print("🔁 Waiting for QR code scan...")
time.sleep(20)

# It must exactly match the name as it appears in WhatsApp
contact_name = "Jai" # 👈 Change this to your contact/group name

search_box = driver.find_element(By.XPATH,'//div[@title="Search input textbox"]')  # Finds the WhatsApp search input using XPath.
search_box.click()    # Clicks on it
search_box.send_keys(contact_name)   # Types the contact name
time.sleep(3)   # Waits 3 seconds for search results to load.

# Locates the exact chat from search results (based on the contact's title)
chat = driver.find_element(By.XPATH,f'//span[@titile={contact_name}]')
chat.click()   # Clicks on it to open the conversation

print(f'\n📥 Reading messages from {contact_name}\n')  # Tells the user in the terminal that messages are being read
time.sleep(5)   # Waits 5 seconds to make sure chat is fully loaded

# Finds all incoming messages (sent to you) in the current chat
# Filters by class message-in (for received messages)
# Extracts the inner text spans (where the actual message text is stored)
# ⚠️ These class names like _11JPr may change in future updates to WhatsApp Web, so the script may break and need updates
messages = driver.find_element(By.XPATH,'//div[contains(@class,"messages-in")]//span[@class,"_11JPr"]')

# Loops through the last 10 received messages, Prints them one by one with numbering in the terminal, msg.text gets the actual text content of each message
for i, msg in enumerate(messages[-1:], 1):
    print(f"{i}.{msg.text}")

# Optional: Close browser after done
# driver.quit()