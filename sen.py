# selenium 3
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
'''

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


def test_eight_components():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    sleep(3)
    # request browser information
    title = driver.title
    assert title == "Web form"

    # establish waiting strategy
    driver.implicitly_wait(10)

    # find an element
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # take action on element
    text_box.send_keys("Selenium")
    driver.implicitly_wait(10)
    submit_button.click()

    sleep(3)
    # request element information
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    driver.implicitly_wait(10)

    # end the session
    driver.quit()


test_eight_components()
