import pandas as np
from rank_bm25 import BM25Okapi
from rank_bm25 import BM25Plus
from rank_bm25 import BM25L
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stop_words = list(stopwords.words('english'))


def word_token(tokens, lemma=False):
    tokens = str(tokens)
    tokens = re.sub(
        r"([\w].)([\~\!\@\#\$\%\^\&\*\(\)\-\+\[\]\{\}\/\"\'\:\;])([\s\w].)", "\\1 \\2 \\3", tokens)
    tokens = re.sub(r"\s+", " ", tokens)
    return " ".join([token for token in word_tokenize(tokens.lower()) if token not in stop_words and token.isalpha()])


def rank_query(query, documents):
    docs = query + documents
    docs = [word_token(d, lemma=True) for d in docs]
    tokenized_corpus = [doc.split(' ') for doc in docs]

    bm25 = BM25Okapi(tokenized_corpus[1:])
    bm25plus = BM25Plus(tokenized_corpus[1:])
    bm25L = BM25L(tokenized_corpus[1:])

    query = tokenized_corpus[0]

    bm25_scores = bm25.get_scores(query)
    bm25plus_scores = bm25plus.get_scores(query)
    bm25L_scores = bm25L.get_scores(query)

    bm25_scores = [(i, v) for i, v in enumerate(bm25_scores)]
    bm25plus_scores = [(i, v) for i, v in enumerate(bm25plus_scores)]
    bm25L_scores = [(i, v) for i, v in enumerate(bm25L_scores)]

    bm25_scores.sort(key=lambda x: x[1], reverse=True)
    bm25plus_scores.sort(key=lambda x: x[1], reverse=True)
    bm25L_scores.sort(key=lambda x: x[1], reverse=True)

    #print(bm25_scores, bm25plus_scores, bm25L_scores)

    return bm25_scores, bm25plus_scores, bm25L_scores


bm_1, _, _ = rank_query('when messi was born', "Lionel Andrés Messi Cuccittini[note 1] (Spanish pronunciation: [ljoˈnel anˈdɾez ˈmesi] (About this soundlisten);[A] born 24 June 1987) is an Argentine professional footballer who plays as a forward and captains both Spanish club Barcelona and the Argentina national team. Often considered the best player in the world and widely regarded as one of the greatest players of all time, Messi has won a record six Ballon d'Or awards,[note 2] and a record six European Golden Shoes. He has spent his entire professional career with Barcelona, where he has won a club-record 34 trophies, including ten La Liga titles, four UEFA Champions League titles and six Copas del Rey. A prolific goalscorer and a creative playmaker, Messi holds the records for most goals in La Liga (438), a La Liga and European league season (50), most hat-tricks in La Liga (36) and the UEFA Champions League (8), and most assists in La Liga (181) and the Copa América (12). He has scored over 700 senior career goals for club and country.")
bm_1 = np.array(bm_1)
bm_1_idx = bm_1[bm_1[:, 1] > 1][:num_paragraphs, 0]  # two most similar
bm_1_idx = np.array(bm_1_idx, dtype=int)
text = ' '.join(text[i] for i in sorted(bm_1_idx))
print('======= BM25 SCORES =======')
print(bm_1)
