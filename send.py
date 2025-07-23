from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def send_message(ad_url, message, creds):
    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)
    # 1. Connexion
    driver.get("https://www.leboncoin.fr/compte/connexion")
    driver.find_element(...).send_keys(creds["login"])
    driver.find_element(...).send_keys(creds["password"])
    driver.find_element(...).click()
    # 2. Aller sur l’annonce et poster le message
    driver.get(ad_url)
    textarea = driver.find_element(...)
    textarea.send_keys(message)
    driver.find_element(...).click()
    driver.quit()
