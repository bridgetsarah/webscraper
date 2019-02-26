from bs4 import BeautifulSoup
import requests  

with open('simple.html') as html_file:                          #Open file object
    soup = BeautifulSoup(html_file, 'lxml')                     #Html parser 'lxml'

#match = soup.div.text                                           #Searches for divs containing 'text'
#print(match)

news = soup.find('div', class_='news')
print(news)
# print article
headline = news.h1.text
print(headline)

#print summary

summary = news.p.text
print(summary)