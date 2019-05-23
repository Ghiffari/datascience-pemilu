# import libraries
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# specify the url
url = 'https://kawalpemilu.org/#pilpres:0'

# The path to where you have your chrome webdriver stored:
webdriver_path = '/Users/macbook/Downloads/chromedriver'

# Add arguments telling Selenium to not actually open a window
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')

# Fire up the headless browser
browser = webdriver.Chrome(executable_path=webdriver_path,
                           options=chrome_options)

# Load webpage
browser.get(url)

# It can be a good idea to wait for a few seconds before trying to parse the page
# to ensure that the page has loaded completely.
time.sleep(10)

# Parse HTML, close browser
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
pretty = soup.prettify()
browser.quit()
# find results within table
results = soup.find('table',{'class':'table'})
rows = results.find_all('tr',{'class':'row'})
array = []
jokowi = []
prabowo = []

# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    satu = data[2].find('span', attrs={'class':'abs'}).getText()
    dua = data[3].find('span', attrs={'class': 'abs'}).getText()
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    satu = int(satu)
    dua = int(dua)
    array.append(wilayah)
    jokowi.append(satu)
    prabowo.append(dua)

# Create Dictionary
my_dict = {'wilayah':array,'jokowi':jokowi,'prabowo':prabowo}
# Create Dataframe
df = pd.DataFrame(my_dict)
# Plot dataframe to histogram
plt.hist([df['jokowi'],df['prabowo']],label=['jokowi','prabowo'],bins=10)
plt.yticks([0,2,4,6,8,10,12,14,16,18,20,22])
plt.xlabel('perolehan suara')
plt.ylabel('frequency')
plt.legend(loc='upper right')
plt.show()

