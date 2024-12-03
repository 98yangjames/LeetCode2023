class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {char:i for i, char in enumerate(order)}


        def is_sorted(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if dic[word1[i]] < dic[word2[i]]:
                    return True
                elif dic[word1[i]] > dic[word2[i]]:
                    return False
            return len(word1) <= len(word2)

        for i in range(len(words)-1):
            if is_sorted(words[i], words[i+1]) == False:
                return False
        return True
            