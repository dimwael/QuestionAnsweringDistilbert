from scraper import mainscraper

user_question = "How many ballons d'Or does Messi have ?"

# Scraping starts :

# Get paragraphs from wikipedia articles using scraping
fetched_answers = mainscraper.fetch_search_wiki(
    user_question=user_question, stops=1)
first_answer = fetched_answers[0]

# Check all paragraphs in our scraped results
for paragraph in first_answer:
    print(paragraph)
    print("**************")
