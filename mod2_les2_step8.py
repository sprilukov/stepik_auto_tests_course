from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import random
import string
import os 
letters = string.ascii_lowercase

with open("test.txt", "w") as file:
    content = file.write("automationbypython")

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type=text]")
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path) 

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла