import pandas as pd
from pandas import ExcelWriter

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../chromedriver.exe")
driver.get(r'https://en.wikipedia.org/wiki/List_of_chapters_in_the_Quran')
table  = driver.find_element_by_tag_name('table')
tbody = table.find_element_by_tag_name('tbody')
rows = tbody.find_elements(By.TAG_NAME, "tr")
titles = []
for row in rows:
    # get Anglicized title(s) and append to titles collection
    title = row.find_elements(By.TAG_NAME, "td")[1]
    titles.append(title.text)

driver.close()


df = pd.read_excel('../data/Quran Database.xlsx')
number_of_data_rows = len(df.index)
for row_number in range(0, number_of_data_rows):
    current_chapter = df.loc[df.index[row_number], 'Chapter']
    df.loc[df.index[row_number], 'Chapter Name'] = titles[current_chapter-1]

df.to_csv ('../data/Quran Database with chapter name.csv', index = False, header=True)