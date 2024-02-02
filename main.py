import re

from src.file.FileReader import FileReader
from src.orph.Checker import Checker
from nltk.tokenize import word_tokenize
import nltk

nltk.download('popular')


def print_p(text):
    for word in text:
        print(word)


if __name__ == '__main__':
    text = FileReader.read_pdf_files("D:\\Download\\testPDF.pdf")
    checker = Checker()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    words = word_tokenize(text)
    print_p(words)
    checker.countWords(words)
