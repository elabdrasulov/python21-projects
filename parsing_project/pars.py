# import csv
# import requests
# from bs4 import BeautifulSoup

# # with open('news.csv', 'w') as file:
# #     pass

# def write_to_csv(dict):
#     with open('news2.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([dict['header']])


# def response(url):
#     # headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
#     response = requests.get(url)
#     return response.text
# def get_info(html):
#     soup = BeautifulSoup(html, 'lxml')
#     block = soup.find_all('div', class_='itemBody')
#     for headers in block:
#         header = headers.find('a').text.strip()
#         data = {'header': header}
#         write_to_csv(data)

# def main():
#     url = 'https://vesti.kg'
#     get_info(response(url))


# main() 

# import csv
# import requests
# from bs4 import BeautifulSoup

# def write_to_csv(data):
#     with open('test.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title']])

# def get_url(url):
#     response = requests.get(url)
#     return response.text

# def get_info(html):
#     soup = BeautifulSoup(html, 'lxml')
#     news_list = soup.find_all('div', class_='itemBlock')

#     for titles in news_list:
#         title = titles.find('div', class_='itemBody').find('a').text.strip()
#         data = {'title': title}
#         write_to_csv(data)
# def main():
#     url = 'https://vesti.kg'
#     get_info(get_url(url))

# main()


import requests
import csv
from bs4 import BeautifulSoup

def get_url(url):
    response = requests.get(url)
    return response.text

def write_to_csv(data):
    with open('titles.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title']])

def get_info(html):
    soup = BeautifulSoup(html, 'lxml')
    news_list = soup.find_all('div', class_="itemBlock")

    for titles in news_list:
        title = titles.find('div', class_="itemBody").find('a').text.strip()
        data = {'title': title}
        write_to_csv(data)

def main():
    url = 'https://vesti.kg/'
    get_info(get_url(url))

main()