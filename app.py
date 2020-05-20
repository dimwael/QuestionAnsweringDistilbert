from pipeline import answer_question
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/question', methods=['GET', 'POST'])
def ask_question():
    question = request.json.get('input_question')
    answer, best_paragraph, url = answer_question(question)
    return jsonify({'link': url, 'text_paragraphs': best_paragraph, 'answer': answer})


if __name__ == '__main__':
    app.run(port=5001)
