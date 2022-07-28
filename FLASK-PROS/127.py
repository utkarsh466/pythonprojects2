from gettext import find
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

browser= webdriver.Chrome("D:\SomeTimesUsedFolders\whjr\pythonprojects2\FLASK-PROS\chromedriver.exe")
url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser.get(url)

time.sleep(10)


def scrape():
    
    headerList=[
        "Proper name","Distance","Mass","Radius","Luminosity"
    ]
    starList=[]
    
    for x in range(2):
        time.sleep(3)
        soup=BeautifulSoup(browser.page_source,"html.parser")
        tableRow=soup.find_all("tr")
        # print(tableRow)
        tableRow.pop(0)
        temp_list=[]
        for tr in tableRow:
            td=tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)
        
      
        index=0
        newlist=[]
        for row in temp_list:
            index=0
            newlist=[]
            for value in row:
                
                if(index==1 or index==3 or index==5 or index==6 or index==7):
                    newlist.append(value)
                index+=1
            index=0
            starList.append(newlist)
        print(starList)
   
    df=pd.DataFrame(starList,columns=headerList)        
scrape()        