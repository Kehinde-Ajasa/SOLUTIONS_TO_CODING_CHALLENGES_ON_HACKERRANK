# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
import itertools
main_word = input('Enter the main word: ')
subordinate_word = input('Enter the subordinate word: ')
words_list = []  # list to save the result of the itertools module
"""function to help identify if the sub-word is an anagram of the main word"""


def find_anagrams(first_word, second_word):
    for i in range(len(first_word), 2, -1):
        sub_words = itertools.permutations(first_word, i)
        for word in sub_words:
            words_list.append(''.join(word))
    return second_word in words_list


print(find_anagrams(main_word, subordinate_word))
