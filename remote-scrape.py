import requests  
from bs4 import BeautifulSoup

url = ('http://www.devbk.me/')
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html_doc, 'html.parser')  #Html Parser
soup.find_all("title")
soup.find_all("p")
soup.find_all("a")

print(BeautifulSoup)