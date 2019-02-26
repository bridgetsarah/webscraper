from bs4 import BeautifulSoup
import requests  

with open('http://www.robotstxt.org/meta.html') as html_file:                          #Open file object
    soup = BeautifulSoup(html_file, 'lxml')                     #Html parser 'lxml'

#match = soup.div.text                                           #Searches for divs containing 'text'
#print(match)

news = soup.find('div', class_='content')
print(news)
