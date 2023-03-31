class Solution(object):
    def isAnagram(self, s, t):        
        dictionary = {}
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        print(dictionary)
        
        new_dictionary = {}
        for j in t:
            if j not in new_dictionary:
                new_dictionary[j] = 1
            else:
                new_dictionary[j] += 1
        print(dictionary)
        print(new_dictionary)
        
        if (dictionary == new_dictionary):
            return True
        
        else:
            return False