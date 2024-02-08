from flask import Flask, request, jsonify

from src.dto.FormMapper import FormMapper
from src.file.FileReader import FileReader
from src.orph.Checker import Checker
from flask_cors import CORS, cross_origin

path = "D:\\Download\\testPDF.pdf"
app = Flask(__name__)
CORS(app)
all_words = []
app.config['CORS_HEADERS'] = 'Content-Type'


# "D:\\Download\\testPDF.pdf"
@app.route('/words', methods=['GET'])
@cross_origin()
def get_all_words():
    global all_words, path
    print(path)
    all_words = []
    text = FileReader.read_pdf_files(path)
    checker = Checker()
    words = text.split(" ")
    all_words = checker.count_words(words)
    all_words = sorted(all_words, key=lambda word: word.normal_form)
    json = []
    for word in all_words:
        json.append({'id': word.id, 'normal_form': word.normal_form, 'number': word.number})
    return jsonify(json)


@app.route('/words/<int:word_id>')
@cross_origin()
def get_one_word(word_id):
    global all_words
    get_all_words()
    word = find(word_id)
    json = {'id': word.id, 'normal_form': word.normal_form, 'number': word.number, 'forms': []}
    for form in word.forms:
        json["forms"].append(FormMapper.convert(form))
    return jsonify(json)


@app.route('/path', methods=['POST'])
@cross_origin()
def set_path():
    global all_words, path
    all_words = []
    json_data = request.get_json()
    print(json_data.get('path'))
    path = json_data.get('path')
    return {"status": "ok"}


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    global all_words
    get_all_words()
    query = request.args.get('query')
    json = []
    for word in all_words:
        if query.lower() in word.normal_form.lower():
            json.append({'id': word.id, 'normal_form': word.normal_form, 'number': word.number})
    return jsonify(json)


def find(target_id):
    global all_words
    for item in all_words:
        if item.id == target_id:
            found_item = item
            return found_item
