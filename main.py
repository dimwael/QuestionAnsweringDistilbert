from scraper import mainscraper
from QA.reader import reader
user_question = "How many ballons d'Or does Lionel Messi win ?"

# Scraping starts :

# Get paragraphs from wikipedia articles using scraping
fetched_answers = mainscraper.fetch_search_wiki(
    user_question=user_question, stops=1)
first_answer = fetched_answers[0]

# Check all paragraphs in our scraped results
# for paragraph in first_answer:
#     print(paragraph)
#     print("**************")


# Use the text reader to extract the correct answer
# testinput is just for testing purposes :
testinput = first_answer[3]

# Call the text reader :
answer = reader.answer(user_question, testinput)
print(answer)
