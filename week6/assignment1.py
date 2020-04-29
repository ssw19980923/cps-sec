from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time
import csv

path = os.getcwd() + "\week6\chromedriver.exe"
driver = webdriver.Chrome(path)


try:
    driver.get("http://www.mgstore.co.kr/")
    time.sleep(7)

    searchIndex = "스케쥴러"
    element = driver.find_element_by_class_name("text")
    element.send_keys(searchIndex)
    driver.find_element_by_xpath('//*[@id="btnSearchTop"]').click()

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    
    file = open("assignment.csv", 'w', newline = "", encoding="utf-8")
    wr = csv.writer(file)
    wr.writerow(["No.", "Brand", "Name", "Price"])
    file.close()

    brand = []
    name = []
    price = []


    for i in range(2):
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        items = bs.find_all("div", class_="space")
        
        for a in items:
            brand.append(a.find("div", class_="txt").find("span", class_="brand").find("strong").text)
            name.append(a.find("div", class_="txt").find("a").find("strong").text)
            price.append(a.find("div", class_="price gd-default").find("span", class_="cost").find("strong").text)



    file = open("assignment.csv", "a", newline="", encoding="utf-8")
    wr = csv.writer(file)

    for i in range(len(brand)):
        wr.writerow([str(i+1), brand[i], name[i], price[i]])
    file.close()
  


finally:
    time.sleep(3)
    driver.quit()