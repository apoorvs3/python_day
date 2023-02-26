import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def initialize_driver():
    email = email_input.get()
    pwd = password_input.get()
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('https://www.amazon.com/')
    driver.find_element(By.XPATH('//*[@id="nav-main"]/div[1]/div/div/div[3]/span[1]/span/input')).click()
    driver.find_element(By.CSS_SELECTOR('#nav-link-accountList')).click()
    driver.find_element(By.CSS_SELECTOR('#ap_email')).send_keys(email)
    driver.find_element(By.XPATH("//input[@id='continue']")).click()
    time.sleep(3)
    driver.find_element()
    driver.find_element(By.CSS_SELECTOR("#ap_password")).send_keys(pwd)
    driver.find_element(By.CSS_SELECTOR('#signInSubmit')).click()


def validate_data():
    df = pd.read_csv('asin.csv')
    asins = df['ASIN'].dropna().to_list()
    if len(asins) != 0:
        for asin in asins:
            pass


window = Tk()
window.title('App Downloader')
window.minsize(height=300, width=200)
window.config(padx=50, pady=50)

email_label = Label(text='Email: ')
email_label.grid(column=0, row=0)
email_input = Entry(width=35)
email_input.grid(column=1, row=0)

password_label = Label(text='Password: ')
password_label.grid(column=0, row=1)
password_input = Entry(width=35)
password_input.grid(column=1, row=1)

# button_validData = Button(text='Validate Data', command=initialize_driver)

sign_in_button = Button(text='Sign in', command=initialize_driver)
sign_in_button.grid(column=0, row=2, columnspan=2)

window.mainloop()
