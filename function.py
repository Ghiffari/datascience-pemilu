import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
from sklearn.linear_model import LinearRegression
def setPlotText(data, x, y, val='', halign='right', valign='bottom', color='black',rotate=0,scale=False):
    for i, v in enumerate(data):
        if(scale==False):
            if(v != 0):
                plt.text(i+(x), v+(y), str(v) + val, horizontalalignment=halign, verticalalignment=valign, color=color, fontweight='bold',rotation=rotate)
        else:
            if(v != 0):
                plt.text(i + (x), v + (y), str(round(v/10000000,2)) + val, horizontalalignment=halign, verticalalignment=valign, color=color,fontweight='bold', rotation=rotate)
def crawlData(url,second=5):
    # specify the url

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
    time.sleep(second)

    # Parse HTML, close browser
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()

    return soup

def estimate_coefficients(x, y):
    # size of the dataset OR number of observations/points
    n = np.size(x)

    # mean of x and y
    # Since we are using numpy just calling mean on numpy is sufficient
    mean_x, mean_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x - n * mean_y * mean_x)
    SS_xx = np.sum(x * x - n * mean_x * mean_x)

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = mean_y - b_1 * mean_x
    print(b_0 + b_1)

    return (b_0, b_1)



def plot_regression_line(x, y, b,xlabel,ylabel):
    # plotting the points as per dataset on a graph
    plt.scatter(x, y, color="green", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="black")

    # putting labels for x and y axis
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # function to show plotted graph
    plt.show()

# Param x,y data sets
def do_regress(x,y,xlabel,ylabel):

    # estimating coefficients
    b = estimate_coefficients(x, y)

    # plotting regression line
    plot_regression_line(x, y, b,xlabel,ylabel)