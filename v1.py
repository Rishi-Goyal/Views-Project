from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

  
# create webdriver object
i = 0
a = ["https://www.youtube.com/embed/epOiQE8O38A","https://www.youtube.com/embed/RQksHlIenpI", "https://www.youtube.com/embed/MGPvv4XgHEc"]

for i in range(100):
    driver = webdriver.Firefox()

    b = random.randint(0,2)

    driver.get(a[b])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    driver.minimize_window()
    i+=1
    time.sleep(300)
    driver.quit()




#element = WebDriverWait(driver,300)
#driver.quit()

#element.send_keys('k')

#action.click(on_element = element)