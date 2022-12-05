
#3
# website: https://www.areavibes.com/pittsburgh-pa/shadyside/crime/
# XPath: html/body/div[5]/div/div[1]/div/div/div[1]/text()
# Crime Rating
import os
from requests.api import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
# chromedriver = "C:/Users/pacer/AppData/Local/Google/Chrome/Application/chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver, chrome_options=options)
browser = webdriver.Chrome(ChromeDriverManager().install())


#Shady Side
url_shady_side = "https://www.areavibes.com/pittsburgh-pa/shadyside/crime/"
shady_side = []
# Crime
browser.get(url_shady_side)
'''
raw = browser.page_source
print (raw)
'''

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[4]/i').text
shady_side.append(html)


# Amenities
browser.get(url_shady_side)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[2]/i').text
shady_side.append(html)

# Cost of Living
browser.get(url_shady_side)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[3]/i').text
shady_side.append(html)

print ('Shady Side Rating')
print(shady_side)

#Squirrel Hill North
url_shill_north = "https://www.areavibes.com/pittsburgh-pa/squirrel+hill+north/livability/"
squirrel_hill_north = []

#Crime
browser.get(url_shill_north)

'''
raw1 = browser.page_source
print (raw1)
'''

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[4]/i').text
squirrel_hill_north.append(html)


# Amenities
browser.get(url_shill_north)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[2]/i').text
squirrel_hill_north.append(html)


# Cost of Living
browser.get(url_shill_north)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[3]/i').text
squirrel_hill_north.append(html)
print ('Squirrel Hill North Rating')
print(squirrel_hill_north)

#Squirrel Hill South
url_shill_south = "https://www.areavibes.com/pittsburgh-pa/squirrel+hill+south/livability/"
squirrel_hill_south = []

#Crime
browser.get(url_shill_south)
'''
raw2 = browser.page_source
print (raw2)
'''
html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[4]/i').text
squirrel_hill_south.append(html)

# Amenities
browser.get(url_shill_south)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[2]/i').text
squirrel_hill_south.append(html)


# Cost of Living
browser.get(url_shill_south)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[3]/i').text
squirrel_hill_south.append(html)

print ('Squirrel Hill South Rating')
print(squirrel_hill_south)


#Oakland

url_oakland = "https://www.areavibes.com/pittsburgh-pa/oakland/livability/"
oakland = []

#Crime
browser.get(url_oakland)
'''
raw = browser.page_source
print (raw)
'''
html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[4]/i').text
oakland.append(html)

# Amenities
browser.get(url_oakland)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[2]/i').text
oakland.append(html)


# Cost of Living
browser.get(url_oakland)

html = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div/nav[2]/a[3]/i').text
oakland.append(html)

print ('Oakland Rating')
print(oakland)

headers = ['Neighbourhood', 'Crime', 'Amenities', 'Cost of Living']

with open('ratings.csv', 'w') as f:
    lines = list()
    lines.append(','.join(headers) + '\n')
    lines.append('Shadyside,' + ','.join(shady_side) + '\n')
    lines.append('Squirrel Hill South,' + ','.join(squirrel_hill_south) + '\n')
    lines.append('Squirrel Hill North,' + ','.join(squirrel_hill_north) + '\n')
    lines.append('Oakland,' + ','.join(oakland))
    f.writelines(lines)


