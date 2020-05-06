import bs4
import requests
import re


def scrape_wiki(link):
    response = requests.get(link)
    lines = []
    if response is not None:
        html = bs4.BeautifulSoup(response.text, 'html.parser')
        title = html.select("#firstHeading")[0].text
        paragraphs = html.select("p")
        for para in paragraphs:
            text = re.sub(r'\[\w+\]', '', para.text)
            text = re.sub(r'\s\s+', '', text)
            text = re.sub(r'\n', '', text)
            if len(text.split()) > 5:
                lines.append(text)
    return link, lines
