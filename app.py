from pipeline import answer_question
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("main_page.html")


@app.route('/question', methods=['GET', 'POST'])
def ask_question():
    question = request.json.get('input_question')
    print(question)
    answer, best_paragraph, url = answer_question(question)
    print(answer)
    print(best_paragraph)
    return jsonify({'link': url, 'text_paragraphs': str(best_paragraph), 'albert': answer})



if __name__ == '__main__':
    app.run()
