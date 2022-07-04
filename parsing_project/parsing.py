import csv
import requests
from bs4 import BeautifulSoup
# import time
# import numpy as np

# time.sleep((30-5)*np.random.random()+5) #from 5 to 30 seconds


def get_html(url):

    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url) #(url, headers = headers)
    # res1 = response.raise_for_status()
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages_ul = soup.find('div', class_="pager-wrap").find('ul')
    last_page = pages_ul.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return int(total_pages)

def write_to_csv(data):
    with open('kivano_notebooks.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow((data['title'],
                         data['photo']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_="list-view")
    products = product_list.find_all('div', class_="item product_listbox oh")
    
    for product in products:
        photo = product.find('div', class_="listbox_img pull-left").find('a').find('img').get('src')
        title = product.find('div', class_="listbox_title oh").find('a').text

        data = {'title': title, 'photo': photo}
        write_to_csv(data)

def main():
    notebooks_url = 'https://www.kivano.kg/noutbuki'
    pages = '?page='
    
    total_pages = get_total_pages(get_html(notebooks_url))

    for page in range(1, total_pages+1):
        url_with_page = notebooks_url + pages + str(page)
        html = get_html(url_with_page)
        get_page_data(html)
main()