
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        new_list = []
        sorted_word = sorted(self.word.lower())
        for item in list:
            sorted_item = sorted(item.lower())
            if sorted_item == sorted_word and item.lower() != self.word.lower():
                new_list.append(item)
        return new_list
