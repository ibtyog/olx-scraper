from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.by import By
from requests_html import HTMLSession
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
import time
SITE_URL = input("Paste olx search url:")
FORM_URL = input("Input google forms url:")
driver = webdriver.Chrome(options=options)


driver.get(SITE_URL)
time.sleep(3)
cookie = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
cookie.click()

lista_nazw = driver.find_elements(By.CSS_SELECTOR, ".css-16v5mdi")
lista_cen = driver.find_elements(By.CSS_SELECTOR, ".css-10b0gli")
lista_adresow = driver.find_elements(By.CSS_SELECTOR, ".css-veheph")
lista_linkow = driver.find_elements(By.CSS_SELECTOR, ".css-rc5s2u")
scrape= []

for row in range(0,len(lista_nazw)):
    scrape.append(lista_nazw[row].text)
    scrape.append(lista_adresow[row].text)
    scrape.append(lista_cen[row].text)
    scrape.append(lista_linkow[row].get_attribute('href'))


driver.get(FORM_URL)
time.sleep(5)
for row in range(0,int(len(scrape)/4)):
    lista_input = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
    lista_input[0].send_keys(scrape[row * 4])
    lista_input[1].send_keys(scrape[row * 4 + 1])
    lista_input[2].send_keys(scrape[row * 4 + 2])
    lista_input[3].send_keys(scrape[row * 4 + 3])
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    time.sleep(2)