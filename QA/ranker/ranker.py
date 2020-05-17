import pandas as pd
import numpy as np
from . import BM25Retriever
from .utils import filter_paragraphs
from .utils import generate_squad_examples
from .utils import _expand_paragraphs


def rank_paragraphs(question, paragraphs):
    """Rank scraped paragraphs and return best one. Use BM25 as algorithm of ranking. 

    Arguments:
        question {String} -- User question
        paragraphs {List} -- List of paragraphs from Web scraper

    Returns:
        List -- returns a list of pydict with the best paragraph and some metadata
    """
    df = pd.DataFrame({'title': 'title', 'paragraphs': paragraphs})
    df = filter_paragraphs(df)
    bm = BM25Retriever(b=0.75, floor=None, k1=2.0, lowercase=False,
                       max_df=0.85, min_df=2, ngram_range=(1, 2),
                       preprocessor=None, stop_words='english',
                       token_pattern='(?u)\\b\\w\\w+\\b',
                       tokenizer=None, top_n=10, verbose=False,
                       vocabulary=None)
    df["content"] = df["paragraphs"].apply(lambda x: " ".join(x))
    df = _expand_paragraphs(df)

    bm.fit(df=df)

    best_idx_scores = bm.predict(query=question)

    results = generate_squad_examples(
        question=question,
        best_idx_scores=best_idx_scores,
        metadata=df,
        retrieve_by_doc=False)

    return results[0]['paragraphs']
