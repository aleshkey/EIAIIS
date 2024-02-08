import datetime
import random
import matplotlib.pyplot as plt
import string
import time

from src.orph.Checker import Checker

all_words = []
x = []
y = []

def test():
    global all_words
    for i in range(2000):
        all_words = []
        generate_words(i)
        checker = Checker()
        start = time.perf_counter_ns()
        checker.count_words(all_words)
        y.append(int(time.perf_counter_ns()) - int(start))
        x.append(i)
        i += 10


def generate_words(number):
    for i in range(number):
        all_words.append(generate_random_word(10))


def generate_random_word(length):
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(length))
    return random_word


if __name__ == '__main__':
    test()
    plt.plot(x, y)

    plt.ylabel('время выполнения(нс)')
    plt.xlabel('количество слов')
    plt.title('тест производительности')

    plt.show()
