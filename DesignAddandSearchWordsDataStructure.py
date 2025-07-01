import re

class WordDictionary:
    def __init__(self):
        self.dic = {}
    def addWord(self, word):
        if word not in self.dic:
            self.dic[word] = word
    def search(self, word):
        store_len = len(word)
        
        word = word.replace('.', '')

        for key in self.dic.keys():
            if word == "" and store_len > 0:
                print(len(key))
                if len(key) == store_len:
                    return True
            if word in key:
                print(word, key)
                if store_len > len(key):
                    return False
                return True
            
            
        
        return False
obj = WordDictionary()
obj.addWord('a')
obj.addWord('ab')
print(obj.search('..'))
