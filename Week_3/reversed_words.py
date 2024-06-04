class Reverse:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse_word_order(self):
        words = self.sentence.split(" ")
        reverse_sentence = ' '.join(reversed(words))
        return reverse_sentence


reverse = Reverse("Hola lucia")
reverse.reverse_word_order()
