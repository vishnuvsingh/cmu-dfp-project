from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import xlsxwriter

url = 'https://www.google.com/search?q=part+time+jobs+at+pittsburgh+for+students&oq=part+time+jobs+at+pittsburgh+' \
      'for+students&aqs=chrome..69i57j0i22i30j0i390.12005j0j7&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUK' \
      'Ewinx6jq9q_7AhVetmMGHZBEAXkQudcGKAJ6BAgMECo&sxsrf=ALiCzsYGJO9XZVU5z7pJmGTBygOTedzu6w:1668506433763#htivrt=jobs' \
      '&fpstate=tldetail&htichips=organization_mid:/m/0cwx_&htischips=organization_mid;/m/0cwx_:Carnegie%20Mellon%20' \
      'University'
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
driver.get(url)
time.sleep(3)

SCROLL_PAUSE_TIME = 0.5

last_height = driver.execute_script("return document.getElementsByClassName"
                                    "('zxU94d gws-plugins-horizon-jobs__tl-lvc')[0].scrollHeight")
while True:
    driver.execute_script('document.getElementsByClassName("zxU94d gws-plugins-horizon-jobs__tl-lvc")[0].scrollTo(0, '
                          + str(last_height) + ')')
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.getElementsByClassName"
                                       "('zxU94d gws-plugins-horizon-jobs__tl-lvc')[0].scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

page_source = driver.page_source
with open("jobs_raw.txt", "w") as f:
    f.write(page_source)
soup = BeautifulSoup(page_source, features='html.parser')
jobs = soup.find_all("div", {"class": "pE8vnd avtvi"})
header = ["Job Title", "Link", "Location", "Organization", "Type", "Date", "Experience Required"]
data = []
for job in jobs:
    data_entry = ['N/A'] * 7
    data_entry[0] = job.find("h2", {"class": "KLsYvd"}).text
    data_entry[1] = job.find("a", {"class": "pMhGee Co68jc j0vryd"}, href=True)['href']
    loc_org_div = job.find_all("div", {"class": "sMzDkb"})
    data_entry[2] = loc_org_div[1].text
    data_entry[3] = loc_org_div[0].text
    type_date_div = job.find_all("div", {"class": "I2Cbhb"})
    for div in type_date_div:
        text = div.text
        if 'ago' in text:
            data_entry[5] = text
        else:
            data_entry[4] = text
    qual_div = job.find_all("div", {"class": "nDgy9d"})
    for div in qual_div:
        text = div.text
        if 'experience' in text.lower() and 'year' in text.lower():
            data_entry[6] = text
            break
    data.append(data_entry)

df = pd.DataFrame(data, columns=header)
writer = pd.ExcelWriter('jobs.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()

