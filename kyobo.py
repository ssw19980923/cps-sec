from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "\week6\chromedriver.exe"
print(path)

driver = webdriver.Chrome(path)
try:
    driver.get("http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.com/")
    time.sleep(7)

    # 검색 후 클릭
    searchIndex = "파이썬"
    element = driver.find_element_by_class_name("main_input")
    element.send_keys(searchIndex)
    driver.find_element_by_class_name("btn_search").click()

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("span", id = "totalpage").text
    print(pages)

    title = []
    for i in range(3):
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        #pageurl 이 복잡한 경우 버튼 클릭하기
        contents = bs.find("div", class_ = "list_search_result").find_all("td", class_="detail")

        title.append("page" + str(i +1))

        for c in contents:
            title.append(c.find("div", class_="title").find("strong").text) #값만 원하므로

  
        driver.find_element_by_xpath('//*[@id="contents_section"]/div[9]/div[1]/a[3]').click() # xpath로 다음 버튼 클릭하기

finally:
    for t in title:
        if t.find("page") != -1:
            print()
            print(t)
        else:
            print(t)
    time.sleep(3)
    driver.quit()