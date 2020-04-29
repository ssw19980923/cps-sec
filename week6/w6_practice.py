from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time
import csv

path = os.getcwd() + "\week6\chromedriver.exe"
driver = webdriver.Chrome(path)


try:
    driver.get("https://music.naver.com/home/index.nhn")
    time.sleep(7)

    searchIndex = "조정석"
    element = driver.find_element_by_class_name("input_text")
    element.send_keys(searchIndex)
    driver.find_element_by_xpath('//*[@id="baseSearchForm"]/fieldset/input[1]').click()
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[3]/a').click()

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
        
    song = []
    no = []
    artist = []
    album = []

    file = open("assignment.csv", 'w', newline = "", encoding="utf-8")
    wr = csv.writer(file)
    wr.writerow(["No.", "Title", "Artist", "Album"])
    file.close()

    for i in range(1):
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        songs = bs.find("tbody").find_all("tr", class_="_tracklist_move ")
        
        for s in songs:
            print(s.find("td", class_="name").find("a", class_="_title").find("span", class_="ellipsis").text)
            """
            song.append(s.find("td", class_="name").find("span", class_="ellipsis").text)
            no.append(s.find("td", class_="order").text)
            artist.append(s.find_all("td", class_="_artist").find("span", class_="ellipsis").text)
            album.append(s.find_all("td", class_="album").find("span", class_="ellipsis").text)

    print(len(song), len(artist), len(album), len(no))
    file = open("assignment.csv", "a", newline="", encoding="utf-8")
    wr = csv.writer(file)
    for i in range(len(song)):
        wr.writerow(no[i], song[i], artist[i], album[i])
    file.close()
    """


finally:
    time.sleep(3)
    driver.quit()
