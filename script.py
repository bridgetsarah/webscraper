from bs4 import BeautifulSoup
import requests  

with open('simple.html') as html_file:                          #Open file object
    soup = BeautifulSoup(html_file, 'lxml')                     #Html parser 'lxml'

print(soup)    