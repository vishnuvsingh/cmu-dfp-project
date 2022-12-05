# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:53:26 2022

@author: janet
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from requests.api import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import pandas as pd
import time
options = Options()
options.add_argument('--headless')
chromedriver="C:/Users/pacer/AppData/Local/Google/Chrome/Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver,chrome_options=options)

# url for shadyside
url = "https://www.redfin.com/neighborhood/156434/PA/Pittsburgh/Shadyside/apartments-for-rent"
# get html for shadyside
browser.get(url)

text = browser.page_source
imgs = r'< img class=" homecard-image placeholder" data-src="(.*?)" alt="Placeholder"'
img = re.findall(imgs,text)
# take the first pic
list_new_img = []
for i in range(0,len(img),2):
    list_new_img.append(img[i])

htmls = []
imgs = []
#get shadyside html and imgs
for j in range(25):
    html = browser.find_element(By.XPATH,'//*[@id="MapHomeCard_{}"]/div/div/div[1]/div[1]/div/div/a'.format(j)).get_attribute('href')
    
    htmls.append(html)

    try:
        img = browser.find_element(By.XPATH,'//*[@id="MapHomeCard_{}"]/div/div/div[1]/div[1]/div/div/a/img'.format(j)).get_attribute('src')
        imgs.append(img)
    except:
        try:
            img = browser.find_element(By.XPATH,'//*[@id="MapHomeCard_{}"]/div/div/div[1]/div[1]/div/div/a/img'.format(j)).get_attribute('data-src')
            imgs.append(img)
        except:
            img = browser.find_element(By.XPATH,'//*[@id="MapHomeCard_{}"]/div/div/div[1]/div[1]/div/div/a/div/img'.format(j)).get_attribute('data-src')
            imgs.append(img)
#imgs = imgs+list_new_img
shady_side = {'urls':htmls,'pics':imgs}
data_links = pd.DataFrame(shady_side)
title_list = []
for i in data_links['urls']:
    browser.get(i)
    time.sleep(5)
    try:
        title = browser.find_element(By.XPATH,'//*[@id="content"]/div[10]/div[2]/div[1]/section/div/div/div/div/header/div/h1/div[1]').get_attribute('title')
    except:
        title = browser.find_element(By.CLASS_NAME, 'property-header').text
    title_list.append(title)
data_links['address'] = title_list
 
list_price = []
list_bed = []
list_baths = []
list_sqFt = []
list_policy1 = []
for i in range(25):
    url = data_links['urls'][i]
    browser.get(url)
    time.sleep(3)
    price = browser.find_element(By.XPATH,'//*[@id="content"]/div[10]/div[2]/div[1]/section/div[1]/div/div/div/div/div[1]/div/span').text
    beds = browser.find_element(By.XPATH,'//*[@id="content"]/div[10]/div[2]/div[1]/section/div[1]/div/div/div/div/div[2]/div').text
    beds = beds.replace('-','--')
    baths = browser.find_element(By.XPATH,'//*[@id="content"]/div[10]/div[2]/div[1]/section/div[1]/div/div/div/div/div[3]/div').text
    sqFt = browser.find_element(By.XPATH,'//*[@id="content"]/div[10]/div[2]/div[1]/section/div[1]/div/div/div/div/div[4]/span').text
    try:
        policy1 = browser.find_element(By.XPATH,'//*[@id="feesAndPolicies-collapsible"]/div[2]/div/div/div[1]/h3').text
    except:
        policy1 = ''
    list_price.append(price)
    list_bed.append(beds)
    list_baths.append(baths)
    list_sqFt.append(sqFt)
    list_policy1.append(policy1)
data_links['price'] = list_price
data_links['bed'] = list_bed
data_links['baths'] = list_baths
data_links['sqFt'] = list_sqFt
data_links['policy'] = list_policy1

data_links.to_csv('shadyside_info.csv')