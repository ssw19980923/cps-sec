from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time 

#chromeDriver

# 파이썬 실행중 경로
path = os.getcwd() + "/chromedriver.exe"

driver = webdriver.Chrome(path)

try:
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100&CONTENTS_NO=2&P_TAB_NO=2#page1")
    time.sleep(5) #로딩 되는 시간에 따라
    #driver.implicitly_wait(10)#페이지가 로딩이 될때까지 기다린 후 작동 (만약10초가 넘어가면 끝)

    html = driver.page_source #request.get().text
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_="pagination").find_all("a")[-1]["href"].split("page")[1] ##page21
    pages = int(pages)
    title = []
    for i in range(3):
        driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100&CONTENTS_NO=2&P_TAB_NO=2#page"+str(i+1))
        time.sleep(5)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")
        conts = bs.find_all("div", class_="txtL")
        title.append("page"+str(i+1))

        for c in conts:
            title.append(c.find("a").text)


finally:
    #time.sleep(3)
    for t in title:
        if t.find("page") != -1: #if 문은 true 일때 동작(뒤의 코드가 참인경우) // 없지 않은 경우에만 하겠다
            print() #한칸 듸어짐
            print(t)
        else:
            print(t)
    driver.quit()
