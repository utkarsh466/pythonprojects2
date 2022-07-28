from gettext import find
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

browser= webdriver.Chrome("D:\SomeTimesUsedFolders\whjr\pythonprojects2\FLASK-PROS\chromedriver.exe")
url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser.get(url)

time.sleep(10)


def scrape():
    
    headerList=[
        "Proper name","Distance","Mass","Radius"
    ]
    starList=[]
    
    for x in range(2):
        time.sleep(3)
        soup=BeautifulSoup(browser.page_source,"html.parser")
        tableRow=soup.find_all("tr")
        print(tableRow)
        # tableRow.pop(0)
    
        for i in tableRow:
            tdTag=i.find_all("td")
            temp=[]
            for j in enumerate(tdTag):
                try:
                    temp.append(j.contents[0])
                except:
                    temp.append("")
        starList.append(temp)
                            
    
    with open("scraper.csv","w") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headerList)
        csv_writer.writerows(starList)        
scrape()        