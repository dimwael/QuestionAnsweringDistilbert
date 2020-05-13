from scraper import mainscraper
from QA.reader import reader
from QA.ranker.ranker import rank_paragraphs
user_question = "When was Barack Obama born ?"

# Scraping starts :

# Get paragraphs from wikipedia articles using scraping
fetched_answers = mainscraper.fetch_search_wiki(
    user_question=user_question, stops=1)

# Use the text ranker to extract the best paragraph
retrieved = rank_paragraphs(user_question, fetched_answers)
print(retrieved[0]['context'])


# Use the text reader to extract the correct answer
print('*********************')
print('Reader .. ')
print('*********************')
# Call the text reader :
answer = reader.answer(user_question, retrieved[0]['context'])
print(answer)
