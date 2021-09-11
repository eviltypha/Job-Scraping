from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup
import sqlite3


con = sqlite3.connect('./JobScraping/db.sqlite3')
cur = con.cursor()

count1 = 0
count2 = 0


def starter(URL):
    split_URL = urlsplit(URL)
    BASE = split_URL.scheme + "://" + split_URL.netloc
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'})

    markup = requests.get(URL, headers=HEADERS).text
    soup = BeautifulSoup(markup, 'html.parser')

    return BASE, soup


def nonInterstingURLs(urls1, urls2, soup):
    for item in soup.select('a'):
        try:
            urls2.append(item['href'])
        except:
            print('Skipping...')

    urls2 = [i for i in urls2 if i not in urls1]

    return urls2


def insertDB(urls1, urls2, BASE):
    global count1
    for i in urls1:
        count1 = count1 + 1
        cur.execute(
            "INSERT INTO posts_interesting_urls VALUES (?, ?, ?)", (count1, BASE, i))

    global count2
    for i in urls2:
        count2 = count2 + 1
        cur.execute(
            "INSERT INTO posts_non_interesting_urls VALUES (?, ?, ?)", (count2, BASE, i))


#########################################################################
# internshala

def internshala(URL):

    BASE, soup = starter(URL)

    urls1 = []
    urls2 = []

    for item in soup.select('div.profile.heading_4_5'):
        urls1.append(item.a['href'])

    urls2 = nonInterstingURLs(urls1, urls2, soup)

    insertDB(urls1, urls2, BASE)


#########################################################################
# iimjobs

def iimjobs(URL):

    BASE, soup = starter(URL)

    urls1 = []
    urls2 = []

    for item in soup.select('a.hidden-xs.mrmob5'):
        urls1.append(item['href'])

    urls2 = nonInterstingURLs(urls1, urls2, soup)

    insertDB(urls1, urls2, BASE)


#########################################################################
# talentrack

def talentrack(URL):

    BASE, soup = starter(URL)

    urls1 = []
    urls2 = []

    for item in soup.select('div.job-listing-new'):
        urls1.append(item.a['href'])

    urls2 = nonInterstingURLs(urls1, urls2, soup)

    insertDB(urls1, urls2, BASE)


internshala("https://internshala.com/internships/computer%20science-internship")
iimjobs("https://www.iimjobs.com/k/finance-and-accounts-jobs-362.html")
talentrack("https://www.talentrack.in/all-job-in-india")

con.commit()
con.close()
