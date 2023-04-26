#import the selenium and datetime library
from selenium import webdriver
from datetime import datetime

#write driver path 
DRIVER = 'chromedriver'

#link of the website you want to screenshot 
SITE_URL = input("Enter the website URL of the want to screenshot:\n>")

#Get the date and time
now = datetime.now()
DATE = now.strftime("%b-%d-%Y_%H-%M")

#redirect driver to url
driver = webdriver.Chrome(DRIVER)
driver.get(SITE_URL)

#get screenshot of the website
screenshot = driver.save_screenshot(f'{DATE}.png')

#close the driver
driver.quit()