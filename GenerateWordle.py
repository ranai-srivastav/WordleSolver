import random

class GenerateWordle:

    word_list = open("Wordle/5_letter_words.txt", "r").read().split()

    def __init__(self):
        self.word = gen_word()

    def gen_word():
        word = random.choice(word_list)
        return word

    
    def score_guess(guess):
        pass
