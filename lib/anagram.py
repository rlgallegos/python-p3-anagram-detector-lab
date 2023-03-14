# your code goes here!

class Anagram:
    def __init__(self, word="listen"):
        self.word = word

    def match(self, word_list):
        new_list = []
        char_list = sorted(self.word)
        
        for word in word_list:
            new_char_list = sorted(word)
            if char_list == new_char_list:
                new_list.append(word)

        return new_list
