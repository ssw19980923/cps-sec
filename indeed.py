import requests
from bs4 import BeautifulSoup
import csv

class Scraper():
    def __init__(self):
        self.url = "https://kr.indeed.com/jobs?q=python&limit=50"

    def getHTML(self, cnt):
        res = requests.get(self.url + "&start=" + str(cnt * 50) )
        if res.status_code != 200:
            print("request error: ", res.status_code)

        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def getPages(self, soup):
        pages = soup.select(".pagination > a")
        return len(pages)

    def getCards(self, soup, cnt):
        jobCards = soup.find_all("div", class_="jobsearch-SerpJobCard")

        jobTitle = []
        jobID = []
        jobLocation = []

        for j in jobCards :
            jobID.append("https://kr.indeed.com/viewjob?jk=" + j["data-jk"]) #id 는 attribute 이므로 받는 방법이 다름, 각j 의 데이터-jk 라는 attribute 찾아서 그 값 넣어줌
            jobTitle.append(j.find("a").text.replace("\n", "")) #개행문자를 없앤다
            if j.find("div", class_="location") != None:
                jobLocation.append(j.find("div", class_="location").text) #nonetype = 값이 없어서 text 반환 불가
            elif j.find("span", class_="location") != None:
                jobLocation.append(j.find("span", class_="location").text)
            
        #print(jobID, jobTitle, jobLocation, len(jobID))
        print(len(jobID), len(jobTitle), len(jobLocation))
        self.writeCSV(jobID, jobTitle, jobLocation, cnt)
        
    def writeCSV(self, jobID, jobTitle, jobLocation, cnt):
        file = open("indeed.csv", "a", newline="", encoding="utf-8")
        wr= csv.writer(file)

        for i in range(len(jobID)):
            wr.writerow([str(i+1+(cnt*50)), jobID[i], jobTitle[i], jobLocation[i]]) 
        
        file.close()

    def scrap(self):
        soupPage = self.getHTML(0)
        pages = self.getPages(soupPage)

        file = open("indeed.csv", 'w', newline = "", encoding="utf-8") #write option = 스크래퍼 호출 돌릴때마다 a 태그일 경우 추가만 되기 때문에 초기화 시켜줌
        wr = csv.writer(file)
        wr.writerow(["No.", "Link", "Title", "Location"])
        file.close()

        for i in range(pages):
            soupCard = self.getHTML(i)
            self.getCards(soupCard, i)
            print(i, "번째 페이지 Done")
        

if __name__ =="__main__":
    s = Scraper()
    s.scrap()