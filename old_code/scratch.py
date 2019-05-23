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
url = 'https://2014.kawalpemilu.org/#0'

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
results = soup.find('table',{'class':'aggregate'})
rows = results.find_all('tr',{'class':'datarow'})
# print(rows)
array = []
jokowi = []
prabowo = []
#
# print(rows)
for r in rows:
    # find all columns per result
    data = r.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
# write columns to variables
    wilayah = data[1].find('a').getText()
    satu = data[2].getText()
    dua = data[10].getText()
    # Remove decimal point
    satu = satu.replace('.','')
    dua = dua.replace('.','')
    # Cast Data Type Integer
    satu = int(satu)
    dua = int(dua)
    array.append(wilayah)
    jokowi.append(satu)
    prabowo.append(dua)

# # Convert to numpy
np_array2 = np.array(array)
np_jokowi2= np.array(jokowi)
np_prabowo2= np.array(prabowo)
# # Naming label
# plt.xlabel('provinsi')
# plt.ylabel('perolehan suara')
#
# # styling x,y value
# plt.xticks(rotation=30,ha='right')
# plt.yticks(np.arange(np_jokowi.min(),np_jokowi.max(),4000000))
#
# # plot data
# plt.plot(np_array,np_jokowi,color='red',label='Jokowi',linestyle='--', marker='o')
# plt.plot(np_array,np_prabowo,color='blue',label='Prabowo',linestyle='--', marker='o')
# plt.legend(loc='upper right')
# plt.yscale('linear')
# plt.show()


