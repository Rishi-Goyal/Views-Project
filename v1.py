from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

  
# create webdriver object
i = 0
#a = ["https://www.youtube.com/embed/epOiQE8O38A","https://www.youtube.com/embed/RQksHlIenpI", "https://www.youtube.com/embed/DrdM2ui0pZ4"]
z= 0
a = ["https://www.youtube.com/embed/B7x6jDqB_Wc"]

for i in range(100):
    driver = webdriver.Firefox()

    #b = random.randint(0,2)
    c = random.randint(220,360)
    #element = WebDriverWait(driver,300)
    driver.get(a[0])
    #element.send_keys('k')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    driver.minimize_window()
    i+=1
    z+=1
    print(z)
    #action.click(on_element = element)
    time.sleep(c)
    driver.quit()









