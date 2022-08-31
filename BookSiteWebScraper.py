from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('http://books.toscrape.com/index.html').text

soup = BeautifulSoup(source, 'lxml')

book_dict = {"Book title": [], "Book price": [], "Book availability": []}

for books in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
    book_title = books.article.h3.text
    book_dict['Book title'].append(book_title)

    book_price = books.article.find('p', class_='price_color').text
    book_dict['Book price'].append(book_price)

    book_avail = books.article.find('p', class_='instock availability').text
    book_dict['Book availability'].append(book_avail)
    
book_table = pd.DataFrame(book_dict)
print(book_table)
