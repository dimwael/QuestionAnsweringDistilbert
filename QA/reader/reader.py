from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

tokenizer = DistilBertTokenizer.from_pretrained(
    'distilbert-base-uncased-distilled-squad')
model = DistilBertForQuestionAnswering.from_pretrained(
    'distilbert-base-uncased-distilled-squad')


def answer(question, text):
    """Text reader using distilbert from transformers

    Arguments:
        question {String} -- Question provided by the user
        text {String} -- Text gathered from the text ranker

    Returns:
        String -- The exact answer from the distilbert
    """
    # Encode question, text
    input_ids = torch.tensor(tokenizer.encode(
        question, text, max_length=256, add_special_tokens=True)).unsqueeze(0)  # Batch size 1
    start_positions = torch.tensor([1])
    end_positions = torch.tensor([3])

    # Run distilbert for text reading
    outputs = model(input_ids, start_positions=start_positions,
                    end_positions=end_positions)
    loss, start_scores, end_scores = outputs[:3]

    # Decode the text
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
    start = torch.argmax(start_scores)
    end = torch.argmax(end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(
        all_tokens[start: end])

    return answer
