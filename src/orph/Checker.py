import pymorphy2

from src.util.Proxy import Word


class Checker:
    morph = pymorphy2.MorphAnalyzer()
    words_num = {}

    words = []

    def countWords(self, a_list):
        for i in range(len(a_list)):
            item = self.morph.parse(a_list[i])[0]
            matching_words = [word for word in self.words if word.normal_form == item.normal_form]
            if len(matching_words) == 0:
                word = Word()
                word.normal_form = item.normal_form
                self.words.append(word)
            matching_words = [word for word in self.words if word.normal_form == item.normal_form]
            for word in matching_words:
                self.check_forms(item, word)
        self.words_num = sorted(self.words_num.items(), key=lambda x : x[0])

        self.pretty_map()

    def morphal(self, word):
        parsed_word = self.morph.parse(word)[0]
        print("Слово:", parsed_word.word)
        print("Лемма:", parsed_word.normal_form)
        print("Часть речи:", parsed_word.tag.POS)
        print("Род:", parsed_word.tag.gender)
        print("Падеж:", parsed_word.tag.case)
        print("Число:", parsed_word.tag.number)
        print()

    def pretty_map(self):
        for key, value in self.words_num:
            print(f"{key}: {value}")

    def check_forms(self, item, word):
        if list(filter(lambda x: item.word in x, [w for w in word.forms if w.word]) :
            pass

    def check_form(self, item, form):
        if item.word != form.word:
            return False
        if item.tag.POS != form.tag.POS:
            return False
        if item.tag.gender != form.tag.gender:
            return False
        if item.tag.case != form.tag.casw:
            return False
        if item.tag.number != form.tag.number:
            return False
        return True
