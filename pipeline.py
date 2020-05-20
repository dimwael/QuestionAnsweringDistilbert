from scraper import mainscraper
from QA.reader import reader
from QA.ranker.ranker import rank_paragraphs
user_question = "what is Schrodinger cat ?"


def answer_question(user_question):
    # Scraping starts :
    # Get paragraphs from wikipedia articles using scraping
    fetched_answers, url = mainscraper.fetch_search_wiki(
        user_question=user_question, stops=1)

    # Use the text ranker to extract the best paragraph
    retrieved = rank_paragraphs(user_question, fetched_answers)

    # Call the text reader :
    answer = reader.answer(user_question, retrieved[0]['context'])
    return str(answer), retrieved[0]['context'], url
