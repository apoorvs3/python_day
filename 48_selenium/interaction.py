from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver')
driver.get('https://en.wikipedia.org/wiki/Main_Page')
num_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount > a:nth-child(1)').text
num_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount > a:nth-child(1)').send_keys()

print(num_articles)
