import os
import re
import sys
from tqdm import tqdm
from tika import parser
import pandas as pd
import uuid
import numpy as np


def generate_squad_examples(question, best_idx_scores, metadata, retrieve_by_doc):
    squad_examples = []

    metadata_sliced = metadata.loc[best_idx_scores.keys()]

    for idx, row in metadata_sliced.iterrows():
        temp = {"title": row["title"], "paragraphs": []}

        if retrieve_by_doc:
            for paragraph in row["paragraphs"]:
                temp["paragraphs"].append(
                    {
                        "context": paragraph,
                        "qas": [
                            {
                                "answers": [],
                                "question": question,
                                "id": str(uuid.uuid4()),
                                "retriever_score": best_idx_scores[idx],
                            }
                        ],
                    }
                )
        else:
            temp["paragraphs"] = [
                {
                    "context": row["content"],
                    "qas": [
                        {
                            "answers": [],
                            "question": question,
                            "id": str(uuid.uuid4()),
                            "retriever_score": best_idx_scores[idx],
                        }
                    ],
                }
            ]

        squad_examples.append(temp)

    return squad_examples


def filter_paragraphs(
    articles,
    drop_empty=True,
    read_threshold=1000,
    public_data=True,
    min_length=50,
    max_length=300,
):
    """
    Cleans the paragraphs and filters them regarding their length

    Parameters
    ----------
    articles : DataFrame of all the articles 


    Returns
    -------
    Cleaned and filtered dataframe

    Examples
    --------
    >>> import pandas as pd
    >>> from cdqa.utils.filters import filter_paragraphs

    >>> df = pd.read_csv('data.csv')
    >>> df_cleaned = filter_paragraphs(df)
    """

    # Replace and split
    def replace_and_split(paragraphs):
        for paragraph in paragraphs:
            paragraph.replace("'s", " " "s").replace("\\n", "").split("'")

        return paragraphs

    # Select paragraphs with the required size
    def filter_on_size(paragraphs, min_length=min_length, max_length=max_length):
        paragraph_filtered = [
            paragraph.strip()
            for paragraph in paragraphs
            if len(paragraph.split()) >= min_length
            and len(paragraph.split()) <= max_length
        ]
        return paragraph_filtered

    # Cleaning and filtering
    articles["paragraphs"] = articles["paragraphs"].apply(replace_and_split)
    articles["paragraphs"] = articles["paragraphs"].apply(filter_on_size)
    articles["paragraphs"] = articles["paragraphs"].apply(
        lambda x: x if len(x) > 0 else np.nan
    )

    # Read threshold for private dataset
    if not public_data:
        articles = articles.loc[articles["number_of_read"] >= read_threshold]

    # Drop empty articles
    if drop_empty:
        articles = articles.dropna(
            subset=["paragraphs"]).reset_index(drop=True)
    articles['content'] = articles['paragraphs'].apply(
        lambda x: " ".join(x))
    return articles


def _expand_paragraphs(df):
    # Snippet taken from: https://stackoverflow.com/a/48532692/11514226
    lst_col = "paragraphs"
    df = pd.DataFrame(
        {
            col: np.repeat(df[col].values, df[lst_col].str.len())
            for col in df.columns.drop(lst_col)
        }
    ).assign(**{lst_col: np.concatenate(df[lst_col].values)})[df.columns]
    df["content"] = df["paragraphs"]
    return df.drop("paragraphs", axis=1)
