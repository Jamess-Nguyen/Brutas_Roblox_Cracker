import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_login():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.roblox.com/login")

    driver.find_element("name", "username").send_keys("failed")
    driver.find_element("name", "password").send_keys("failed")
    driver.find_element("name", "password").send_keys("\n") 

    driver.implicitly_wait(5)

    time.sleep(10)  

    if "Home" in driver.title:
        print("Successfully logged in.")
    else:
        print("Login failed.")


if __name__ == "__main__":
    test_login()
    test_login()
