import io
import psycopg2

from flask import Flask, request, jsonify, flash, url_for
from werkzeug.datastructures import FileStorage

from src.dto.FormMapper import FormMapper
from src.file.FileReader import FileReader
from src.orph.Checker import Checker
from src.util.Proxy import Word
from src.Constants import Constants
from flask_cors import CORS, cross_origin

path = "C:\\Learning\\EASIS\\FirstLab\\testPDF.pdf"
app = Flask(__name__)
CORS(app)
file: FileStorage

app.config['CORS_HEADERS'] = 'Content-Type'
text = ''


# "D:\\Download\\testPDF.pdf"
@app.route('/words', methods=['GET'])
@cross_origin()
def get_all_words():
    result = get_words_nf_from_db()
    json = []
    for word in result:
        json.append({'id': word[0], 'normal_form': word[1], 'number': word[2]})
    return jsonify(json)


def get_words_nf_from_db():
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        dbname="exhibition_db",
        user="aleshkey",
        password="lEsha6012004")

    cur = conn.cursor()
    cur.execute("SELECT * FROM words")
    rows = cur.fetchall()
    result = [list(row) for row in rows]
    result = sorted(result, key=lambda word: word[1])
    cur.close()
    conn.close()
    return result


def get_forms_from_bd(id):
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        dbname="exhibition_db",
        user="aleshkey",
        password="lEsha6012004")

    cur = conn.cursor()
    cur.execute("SELECT * FROM wordforms WHERE word_id = %s", (id,))
    rows = cur.fetchall()
    result = [list(row) for row in rows]
    cur.close()
    conn.close()
    return result


@app.route('/words/<int:word_id>')
@cross_origin()
def get_one_word(word_id):
    word = find(word_id)
    json = {'id': word[0], 'normal_form': word[1], 'number': word[2], 'forms': []}
    forms = get_forms_from_bd(word[0])
    for form in forms:
        json["forms"].append(FormMapper.convert(form))
    return jsonify(json)


""""@app.route('/path', methods=['POST'])
@cross_origin()
def set_path():
    global all_words, path
    all_words = []
    json_data = request.get_json()
    print(json_data.get('path'))
    path = json_data.get('path')
    return {"status": "ok"}
"""


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    words = get_words_nf_from_db()
    query = request.args.get('query')
    json = []
    for word in words:
        if query.lower() in word[1].lower():
            json.append({'id': word[0], 'normal_form': word[1], 'number': word[2]})
    return jsonify(json)


def find(target_id):
    words = get_words_nf_from_db()
    for item in words:
        if item[0] == target_id:
            found_item = item
            return found_item


@app.route('/path', methods=['POST'])
@cross_origin()
def upload():
    global file
    clean_db()
    if request.method == 'POST':
        file = request.files['file']
        if file and verify_ext(file.filename):
            try:
                pdf = io.BytesIO(file.read())
                pdf.name = 'temp.pdf'
                pdf.seek(0)
                push_words_into_db(FileReader.process_pdf_file(pdf))
            except Exception as e:
                flash("Read file error", category='error')
        else:
            flash("Invalid file format", category='error')
    return {"status": "ok"}


def verify_ext(filename):
    ext = filename.rsplit('.', 1)[1]
    if ext not in ['pdf', 'PDF']:
        return False
    return True


def push_words_into_db(pdf_text):
    checker = Checker()
    words = pdf_text.split(" ")
    words_from_pdf = checker.count_words(words)
    words_from_pdf = sorted(words_from_pdf, key=lambda word: word.normal_form)

    word_entries = []
    word_forms_entries = []
    for word in words_from_pdf:
        word_entries.append((word.id, word.normal_form, word.number))
        for form in word.forms:
            form_str = str(form.word)
            tag = form.tag
            number = getattr(tag, 'number', None)
            gender = getattr(tag, 'gender', None)
            case = getattr(tag, 'case', None)
            POS = getattr(tag, 'POS', None)
            animacy = getattr(tag, 'animacy', None)
            degree = getattr(tag, 'degree', None)
            tense = getattr(tag, 'tense', None)
            aspect = getattr(tag, 'aspect', None)
            mood = getattr(tag, 'mood', None)
            word_forms_entries.append(
                (word.id, form_str, number, gender, case, POS, animacy, degree, tense, aspect, mood))

    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        dbname="exhibition_db",
        user="aleshkey",
        password="lEsha6012004"
    )
    cur = conn.cursor()

    # Create the Words table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS Words
                           (word_id SERIAL PRIMARY KEY, base_form VARCHAR, count INT)''')

    # Create the WordForms table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS WordForms
                           (form_id SERIAL PRIMARY KEY, word_id INT REFERENCES Words(word_id), form VARCHAR,  "number" VARCHAR, gender VARCHAR, "case" VARCHAR, POS VARCHAR, animacy VARCHAR, "degree" VARCHAR, tense VARCHAR, aspect VARCHAR, mood VARCHAR)''')

    # Insert the word entries into the database
    cur.executemany('INSERT INTO Words (word_id, base_form, count) VALUES (%s, %s, %s)', word_entries)

    # Insert the word forms into the database
    cur.executemany(
        'INSERT INTO WordForms (word_id, form, "number", gender, "case", POS, animacy, "degree", tense, aspect, mood) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        word_forms_entries)

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()


def clean_db():
    conn = psycopg2.connect(
        host="localhost",
        port="5435",
        dbname="exhibition_db",
        user="aleshkey",
        password="lEsha6012004")

    cur = conn.cursor()
    cur.execute("DELETE FROM WordForms")
    cur.execute("DELETE FROM Words")

    conn.commit()

    cur.close()
    conn.close()


@app.route('/words', methods=['POST'])
@cross_origin()
def update_db():
    forms_data = request.get_json()
    print(forms_data)
    new_forms = to_bd_info_view(forms_data)

    conn = psycopg2.connect(
        host='localhost',
        port='5435',
        database='exhibition_db',
        user='aleshkey',
        password='lEsha6012004'
    )

    cursor = conn.cursor()

    sql_query = """
        UPDATE wordforms
        SET
            "number" = %s,
            gender = %s,
            "case" = %s,
            pos = %s,
            animacy = %s,
            "degree" = %s,    
            tense = %s,
            aspect = %s,
            mood = %s
        WHERE
            word_id = %s AND
            form = %s
    """

    for form_data in new_forms:
        cursor.execute(sql_query, (form_data["number"], form_data["gender"],
                                   form_data["case"], form_data["pos"], form_data["animacy"], form_data["degree"],
                                   form_data["tense"], form_data["aspect"], form_data["mood"], form_data["word_id"],
                                   form_data["form"]))

    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "ok"}


def to_bd_info_view(list):
    converted_forms = []
    for form in list:
        converted_form = {
            'word_id': form.get('word_id', None),
            'form': form.get('form', None),
            'number': swap_dict(Constants.number).get(form.get('number', None), None),
            'gender': swap_dict(Constants.gender).get(form.get('gender', None), None),
            'case': swap_dict(Constants.case).get(form.get('case', None), None),
            'pos': swap_dict(Constants.part_of_speech_map).get(form.get('pos', None), None),
            'animacy': swap_dict(Constants.animation).get(form.get('animacy', None), None),
            'degree': None,
            'tense': swap_dict(Constants.time).get(form.get('time', None), None),
            'aspect': swap_dict(Constants.type).get(form.get('type', None), None),
            'mood': swap_dict(Constants.inclination).get(form.get('inclination', None), None)
        }
        converted_forms.append(converted_form)
        print(converted_forms)
    return converted_forms


def swap_dict(dictionary):
    swapped_dict = {value: key for key, value in dictionary.items()}
    return swapped_dict


@app.route('/words/save', methods=['POST'])
@cross_origin()
def save_file():
    file = request.files['file']
    file.save('C:\\Learning\\EASIS\\FirstLab\\src\\report_files\\' + file.filename)
    return {'message': 'Файл сохранен'}
