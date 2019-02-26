from bs4 import BeautifulSoup
import requests  

with open('simple.html') as html_file:                          #Open file object
    soup = BeautifulSoup(html_file, 'lxml')                     #Html parser 'lxml'
# unknown issue - resolving soon
for article in = soup.find_all('div', class_='news'):
    headline = article.news.h1.text
    print(headline)

    summary = article.news.p.text
    print(summary)

    print()
