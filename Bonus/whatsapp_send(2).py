# importing selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
service=Service(r"C:\Users\jidendiran\Downloads\Chrome Driver\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.binary_location=r"C:\ChromePortable\chrome-win64\chrome.exe"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--user-data-dir=whatsapp_profile")
options.add_argument("--start-maximized")
driver=webdriver.Chrome(service=service, options=options)

# Open WhatsApp Web (or reuse tab if it's already logged in)
driver.get("https://web.whatsapp.com")
time.sleep(15)

# Give the exact contact name
contact="Jai"
message="Hello from Python (using selenium)"

# Search for contact
wait=WebDriverWait(driver,60)
search_box=wait.until(EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')))
search_box.click()
search_box.send_keys(contact)
time.sleep(5)

# Click the contact
contact_element=wait.until(EC.presence_of_element_located((By.XPATH,f'//span[@title="{contact}"]')))
contact_element.click()
time.sleep(5)

# Type the message
# Wait for message input box
input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
input_box.send_keys(message)
time.sleep(5)

# Press send
send_bt=wait.until(EC.presence_of_element_located((By.XPATH,'//span[@data-icon="send"]')))
send_bt.click()
time.sleep(5)

print("✅ Message sent successfully!")