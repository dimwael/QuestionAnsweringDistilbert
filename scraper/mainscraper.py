from googlesearch import search
from .wiki_scraper import scrape_wiki
import requests


def fetch_search_wiki(user_question, tld='com', lang='en-US', safe='on', stops=1):
    """Fetch wikipedia for articles using google SE

    Arguments:
        user_question {String} -- User query

    Keyword Arguments:
        tld {str} --  tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain. (default: {'com'})
        lang {str} -- lang stands for language of the search (default: {'en-US'})
        safe {str} -- safe search (default: {'on'})
        stops {int} -- number of result we want to gather(default: {3})
    """
    urls = search('wikipedia:' + user_question, tld=tld,
                  lang=lang, safe=safe, stop=stops)
    articles = []

    print('************************************** ')
    print("Getting Wiki Articles")
    print('************************************** \n')

    for url in urls:
        print(url)
        link, paragraphs = scrape_wiki(url)
        articles.append(paragraphs)
    return articles
