# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:19:37 2021

@author: ht
"""

from selenium import webdriver
import pandas as pd

path = "D:\Icon\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.amazon.in/gp/bestsellers/books/")

titles = driver.find_elements_by_xpath('//div[@data-rows="1"]')
prices = driver.find_elements_by_xpath('//span[@class="p13n-sc-price"]')

#print(titles[0].text)
#print(prices[0].text)
print(len(titles))
print(len(prices))


data = {}
df = pd.DataFrame (data, columns = ['Title','Price'])

for i in range(len(titles)):
    new_row = {'Title':titles[i].text,'Price':prices[i].text}
    df = df.append(new_row, ignore_index=True)

print(df)
df.to_csv("Books Prices.csv")

driver.close()
