# Given a string s find the length of the longest substring without repeating characters

input = "abcabcbb"

def return_dic(input):
    dic = {}
    for i in input:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

def find(input):
    window = set()
    if len(input) == 1:
        return 1
    if len(input) == 0:
        return 0
    left, right = 0, 0
    max_length = 0
    while right < len(input):
        # if not move the right pointer
        if input[right] not in window:
            window.add(input[right])
            if right - left + 1 > max_length:
                max_length = right - left + 1
            right += 1
        else:
            #if duplicate, move the left pointer
            window.remove(input[left])
            left += 1
    return max_length
    #print(len(window))
print(find("abcabcbb"))

        

            

    
    
