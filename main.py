import re

from src.file.FileReader import FileReader
from src.orph.Checker import Checker
from nltk.tokenize import word_tokenize
import nltk



def print_p(text):
    for word in text:
        print(word)


if __name__ == '__main__':
    text = FileReader.read_pdf_files("D:\\Download\\testPDF.pdf")
    checker = Checker()
    text = text.replace("\n", " ")
    text = text.replace(" - ", " ")
    text = text.replace(" -", "-")
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = re.sub(r"\s+", " ", text)
    words = text.split(" ")
    words = checker.countWords(words)
    for word in words:
        print(word)
        print(word.forms)
        print()
