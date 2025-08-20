from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start browser
driver = webdriver.Chrome()
driver.get("http://demo.testfire.net/")
visited = []

# Record page info
def record():
    visited.append((driver.current_url, driver.title))

# Home
record()

# Login page
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(1)
record()

# Do login
driver.find_element(By.NAME, "uid").send_keys("admin")
driver.find_element(By.NAME, "passw").send_keys("admin" + Keys.RETURN)
time.sleep(1)
record()

# Navigate 2 more links
driver.find_element(By.LINK_TEXT, "View Account Summary").click()
time.sleep(1)
record()

driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
time.sleep(1)
record()

# Print visited pages
for url, title in visited:
    print(url, "-", title)

# Close
driver.quit()