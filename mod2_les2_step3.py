from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    print (x)
    z_element = browser.find_element(By.ID, "num2")
    z = z_element.text
    print (z)
    y = str(int(x)+int(z))
    print (y)
 

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()


