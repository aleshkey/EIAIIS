import re

import PyPDF2


class FileReader:
    @staticmethod
    def read_pdf_files(path):
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                t = page.extract_text()
                text = text + t
        text = text.replace("\n", " ")
        text = text.replace(" - ", " ")
        text = text.replace(" -", "-")
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace(",", "")
        text = text.replace("!", "")
        text = text.replace("'", "")
        text = text.replace('"', "")
        text = text.replace('<', "")
        text = text.replace('>', "")
        text = text.replace('+', "")

        text = re.sub(r"\s+", " ", text)
        return text
