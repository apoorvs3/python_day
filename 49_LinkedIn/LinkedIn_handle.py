import os
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv
from Initializer import InitMe


class LinkedIn(InitMe):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.driver.get("https://in.linkedin.com/")
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def log_in(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#session_key").send_keys(os.getenv("user"))
        self.driver.find_element(By.CSS_SELECTOR, "#session_password").send_keys(os.getenv("pwd"))
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]').click()

    def job_portal(self):
        self.driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div').click()
        self.driver.find_element(By.XPATH, '//div[@class="relative"]/input[starts-with(@id, "jobs-search")]').send_keys(os.getenv('job'))
        time.sleep(3)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        ActionChains(self.driver).send_keys("London").perform()
        time.sleep(3)
        ActionChains(self.driver).send_keys("/").perform()
        time.sleep(2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/ul/li[7]/div/span/button").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/ul/li[7]/div/div/div/div/div/form/fieldset/div/ul/li[@class='search-reusables__collection-values-item'][2]/input").click()
        self.driver.find_element(By.XPATH, "//div[@id='search-reusables__filters-bar']/ul/li[7]/div/div/div/div/div/form/fieldset/div/button[2]").click()
        # self.driver.find_element(By.XPATH, '//*[starts-with(@id, "jobs-search-box-location-id")]').send_keys('London')
        ActionChains(self.driver).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
        time.sleep(500)