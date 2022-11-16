from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


def radio_button(self):
    return self.driver.find_element(By.CSS_SELECTOR, "input[value='radio1']")
