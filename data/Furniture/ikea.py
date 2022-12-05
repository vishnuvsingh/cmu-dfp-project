# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:17:43 2022

@author: Haowen Wu
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
urls = ['https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ast001&page=4',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Afu001&page=3',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Akt001&page=3',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Atl001&page=2',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Aba001&page=2',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ade001&page=2',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Aka001&page=2',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Abm001&page=2',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3A700291',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Alc001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Aod001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ali001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ass001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ahe001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Abc001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Ahi001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Arm001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3Awt001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3App001',
       'https://www.ikea.com/us/en/cat/lowest-price/?filters=f-subcategories%3A36812']
driver = webdriver.Chrome()
driver.get(urls[0])#have to get it twice
time.sleep(5)
store_button = driver.find_element(By.CLASS_NAME, 'navigation-button__label')
store_button.click()
time.sleep(2)
input_text = driver.find_element(By.CLASS_NAME, 'geo-ingka-search__input')
input_text.send_keys('15213')
input_text.send_keys(Keys.ENTER)
time.sleep(5)
button = driver.find_element(By.ID, 'geo-market')
button.click()

delivery_button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/div[1]/div[2]/div/span')
delivery_button.click()
time.sleep(2)
input_text = driver.find_element(By.ID, 'zip')
input_text.send_keys('15213')
input_text.send_keys(Keys.ENTER)
time.sleep(5)

product_list = []
a_list = []
price_list = []
delivery_list = []
in_stock_list = []
for url in urls:
    driver.get(url)
    driver.refresh()
    time.sleep(5)
    product_list += driver.find_elements(By.CLASS_NAME, 'pip-header-section')
    a_list += driver.find_elements(By.CLASS_NAME, 'pip-product-compact__wrapper-link')
    price_list += driver.find_elements(By.CLASS_NAME, 'pip-compact-price-package__price-wrapper')
    delivery_list += driver.find_elements(By.XPATH, '/html/body/main/div/div/div[3]/div[1]/div/div[3]/div//div/div[2]/div[1]/span/span[1]')
    in_stock_list += driver.find_elements(By.XPATH, '/html/body/main/div/div/div[3]/div[1]/div/div[3]/div//div/div[2]/div[2]/span/span[1]')

title_list = []
description_list = []
for product in product_list:
    title_list.append(product.text.split(',')[0].replace('\n', ' '))
    try:
        description_list.append(product.text.split(',')[1].strip(' \n"'))
    except:
        description_list.append('No detail')
        
link_list = []
for a in a_list:
    link_list.append(a.get_attribute('href'))

df = pd.DataFrame(columns=['Title', 'Link', 'Description',
                               'Price', 'Delivery', 'In Stock'])
for title, link, description, price, delivery, in_stock in zip(title_list, link_list, description_list,
                                                                  price_list, delivery_list, in_stock_list):
    df.loc[len(df.index)] = [title, link, description, 
                             price.text, delivery.text, in_stock.text] 
df.to_csv('ikea_funiture.csv', encoding = 'utf-8-sig')
print(len(in_stock_list))