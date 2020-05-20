from transformers import pipeline


def summarize_data(data):
    print(data)
    smr_t5 = pipeline(task="summarization", model="t5-small")
    smt5 = smr_t5(data, max_length=150)
    print(smt5[0]['summary_text'])
