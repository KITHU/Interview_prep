"""
   Paridrome Word is a word that is the same even in reverse
   i.e: madam
"""

# Recursive method

def isparidrome(word):
    # word with 1 or 0 caracters is already a paridrome so return True
    if len(word)==0 or len(word) ==1:
        return True
    if word[0] == word[len(word)-1]:
        # if first character and last one are equal then we recurse shrinking word
        return isparidrome(word[1:len(word)-1])
    return False

print(isparidrome("madam")) # True