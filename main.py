from QA import BM25Retriever
import pandas as pd
import numpy as np
from ast import literal_eval
from QA.utils import filter_paragraphs
from QA.utils import generate_squad_examples
from QA.utils import _expand_paragraphs
from QA import reader

df = pd.read_csv('bnpp_newsroom-v1.1.csv',
                 converters={'paragraphs': literal_eval})

#df = _expand_paragraphs(df)

df = df[['title', 'paragraphs']]
df = filter_paragraphs(df)


bm = BM25Retriever(lowercase=True, ngram_range=(1, 2),
                   max_df=0.85, stop_words='english')
bm.fit(df=df)

query = 'Since when does the Excellence Program of BNP Paribas exist?'
best_idx_scores = bm.predict(query=query)
print('**************************')
res = generate_squad_examples(
    question=query,
    best_idx_scores=best_idx_scores,
    metadata=df,
    retrieve_by_doc=False,
)


print("*****************************")
# print(res[0]['paragraphs'])
print('**************************')
best_answers = res[0]['paragraphs'][0]['context'] + \
    res[1]['paragraphs'][0]['context']
print(best_answers)
answer = reader.answer(query, best_answers)
print(answer)

# for element in res[:10]:
#     print(element['title'])
#     print('**************************')
# input_data = res[0]+res[1]
