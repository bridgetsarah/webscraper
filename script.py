import requests                                              #Standard library import
from Beautifulsoup import BeautifulSoup                               #Third-party import - library
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

page_link ='http://devbk.me'

#fetch the content from url

page_response = requests.get(page_link, timeout=30)
page_content = BeautifulSoup(page_response.content, "html.parser")

entry content = page_content.find_all(class_='entry-content')

#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]