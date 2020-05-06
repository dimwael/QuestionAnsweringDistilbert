from bs4 import BeautifulSoup as bs
import requests


url = "https://www.moneycontrol.com/news/politics/"
page = "moneycontrol"


def scrape_money():
    r = requests.get(url)
    sp = bs(r.content, 'xml')
    head = sp.findAll('li', {'class': 'clearfix'})
    articles = sp.findAll('div', {'itemprop': 'articleBody'})

    print(head)
    return head, articles


def scrape_quora():
    url = "https://www.quora.com/topic/Web-Development"
    page = "https://www.quora.com"
    source = "Quora"
    source1 = "Quora"
    r = requests.get(url)
    sp = bs(r.content, 'xml')

    ass = sp.findAll('a', attrs={'class': 'question_link'})

    for Qlink in ass:
        Qhref = Qlink['href']

        FinalLink = page+Qhref
        r1 = requests.get(FinalLink)
        sp1 = bs(r1.content, 'html5lib')
        span1 = sp1.findAll(
            'p', attrs={'class': 'ui_qtext_para u-ltr u-text-align--start'})

        text1 = span1[0].text
        print(text1)


if __name__ == '__main__':
    scrape_quora()
