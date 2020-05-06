import requests
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
from requests_html import HTMLSession
session = HTMLSession()


def get_search_results(user_query):
    search_query = user_query.replace(' ', '-')
    search_query = "https://www.quora.com/"+search_query
    return search_query


def get_answer(user_query):
    search_query = get_search_results(user_query)
    resp = session.get(search_query)
    resp.html.render()
    #sp = bs(content.content, 'xml')
    # print(sp)
    # span1 = sp.findAll(
    #    'span', attrs={'class': 'rendered_qtext'})
    # print(span1)

    http_encoding = resp.encoding if 'charset' in resp.headers.get(
        'content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(
        resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(
        resp.content)
    with open('test.txt', 'w')as f:
        f.write(soup.text)

    # print(soup)
    companyFirstDescr = soup.find_all('span', {'class': 'rendered_qtext'})
    print('\n *********************************** \n')
    for e in companyFirstDescr:
        print(e)
        print('****************************')


get_answer('who is messy')
