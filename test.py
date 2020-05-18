from summarizer.summarizer import summarize_data

from scraper import mainscraper
user_question = "what is Schrodinger cat ?"

# Scraping starts :

# Get paragraphs from wikipedia articles using scraping
fetched_answers = mainscraper.fetch_search_wiki(
    user_question=user_question, stops=1)

data = ''.join([s for s in fetched_answers if isinstance(s, str)])
print(fetched_answers[0])
print(len(data))

summarize_data(fetched_answers[0])
