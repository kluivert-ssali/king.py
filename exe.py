def palindrome(word):
    if word == word[::-1]:
        if type(word) == str:
            return True
        else:
            return "enter a word"
    else:
        return False
print (palindrome("assa"))
print (palindrome("eye"))
print (palindrome("Dave"))