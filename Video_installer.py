link = input("Lütfen link giriniz: \t")
# Kütüphaneler

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Driver yolu giris
browser = webdriver.Edge('msedgedriver.exe')
# Site giris
browser.get("https://y2down.cc/en/")
time.sleep(2)

link_gir = browser.find_element(By.ID, 'link')
link_gir.send_keys(link)

# Butona tıklama
browser.find_element(By.CLASS_NAME, 'strong').click()
time.sleep(16)

# 2. sınıf adına sahip öğeyi bul
second_element = browser.find_elements(By.CLASS_NAME, 'strong')[1]

# öğeye tıkla
second_element.click()
time.sleep(20)
