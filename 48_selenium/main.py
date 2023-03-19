from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = 'chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)
# driver.get('https://www.amazon.com/DOLDRUMS-DOLOROUS-STRAINS-RISITINA/dp/B0BCDGWK8S/?_encoding=UTF8&pd_rd_w=2SLgM&content-id=amzn1.sym.ba25a0fb-eeb9-4762-9c76-8ca869df5234&pf_rd_p=ba25a0fb-eeb9-4762-9c76-8ca869df5234&pf_rd_r=N35WEHYG0PK5S28GJNPF&pd_rd_wg=HZ4o4&pd_rd_r=30128f12-e9bd-42a5-bdd2-81358a77c45b&ref_=pd_gw_exports_top_sellers_unrec')
#
# price = driver.find_element(By.XPATH, '//*[@id="a-autoid-3-announce"]/span[2]/span')
# print(price.text)

driver.get('https://www.python.org/')
time_list = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']//ul[@class='menu']//time")
event_list = driver.find_elements(By.XPATH, "//div[@class='medium-widget event-widget last']//ul[@class='menu']//a")
result_dict = dict()
data_dict = dict()
for idx, data in enumerate(time_list):
    result_dict[idx] = {"time": time_list[idx].text, "name": event_list[idx].text}

print(result_dict)