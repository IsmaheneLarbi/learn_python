from random import shuffle

def wordplay(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)

words = ["beetroot", "carrots", "potatoes"]
anagrams = []

#for loops
# for word in words:
#     anagrams.append(wordplay(word))
# print(anagrams)

#map

#print(list(map(wordplay, words)))

#comprehension
print([wordplay(word) for word in words])