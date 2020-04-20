import csv
import requests
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

    def getHTML(self):
        res = requests.get(self.url)
        if res.status_code !=200:
            print("request error: ", res.status_code)
        
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def getCards(self, soup):
        movieCards = soup.find_all("td", class_="titleColumn")
        ratingCards = soup.find_all("td", class_="ratingColumn imdbRating")

        title = []
        year = []
        rating = []

        for m in movieCards:
            title.append(m.find("a").text)
            year.append(m.find("span", class_="secondaryInfo").text)
            
        for r in ratingCards:
            rating.append(r.find("strong").text)

        print(rating, title)
        print(len(title), len(year), len(rating))
        self.writeCSV(title, year, rating)
    
    def writeCSV(self, title, year, rating):
        file = open("imdb.csv", "a", newline="", encoding='utf-8')
        wr = csv.writer(file)

        for i in range(len(title)):
            wr.writerow([str(i+1), title[i], year[i], rating[i]])
        file.close()

    def scrap(self):
        soupPage = self.getHTML()

        file = open("imdb.csv", "w", newline = "", encoding='utf-8')
        wr = csv.writer(file)
        wr.writerow(["Rank, Title, Year, Rating"])
        file.close()

        soupCard = self.getHTML()
        self.getCards(soupCard)
if __name__ == "__main__":
    s = Scraper()
    s.scrap()