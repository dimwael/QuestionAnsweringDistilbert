from googlesearch import search
import wiki_scraper
import requests


def fetch_search(user_question):
    urls = search(user_question, tld='com', lang='en-US', safe='on', stop=15)
    articles = []
    for url in urls:
        if 'wikipedia' in url:
            link, article = wiki_scraper.scrape_wiki(url)
            articles.append(article)
        print('************************************** \n')
        print("Getting Wiki Articles")
        print('************************************** \n')

