# Camby Abell
# soundex.py template
# CSCI 4140


import sys
import nltk
import re
import itertools

# Define any global helper strings at this point
vowels = "aeiouy"

# Define tuple list and mapping code to create dictionary for consonant
# transformations at this point
new_dict = {}
tuples_list = [(['b', 'f', 'p', 'v'], '1'),
    (['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'], '2'),
    (['d', 't'], '3'),
    (['l'], '4'),
    (['m', 'n'], '5'),
    (['r'], '6')]

for lst, key in tuples_list:
    for i in lst:
        new_dict[i] = key


# function that takes token, transforms it into its new form, and returns it
def wordmap(token):
    first_letter = token[0]
    tail = token[1:]

    # Remove all h and w that is not the first letter
    for ch in tail:
        if ch == 'h' or ch == 'w':
            tail = tail.replace(ch, '')


    # Replace all remaining consonants with digits 
    for value, key in new_dict.items():
        for ch in tail:
            if ch == value:
                tail = tail.replace(ch, key)


    # Concatenate the first letter with the remaining digits
    new_wrd = first_letter + tail
    for ch in new_wrd:
        if ch in vowels:
            new_wrd = new_wrd.replace(ch, '')

    
    # Remove all adjacent same digits, replace with one digit
    new_wrd = ''.join(i for i, _ in itertools.groupby(new_wrd))


    # If result is less than 3 digits, append zeros until 3 digits
    # are present
    while len(new_wrd) < 4:
        new_wrd = new_wrd + '0'


    # If more than three digits, reduce to 3 digits
    new_wrd = new_wrd[:4]    

    new_wrd[0] = first_letter
    
    return new_wrd


# Driver code for the program
# sys.argv[1] should be the name of the input file
# sys.argv[0] will be the name of this file


for line in open(sys.argv[1]).readlines():
    text = nltk.word_tokenize(line.lower())
    for token in text:
        print (wordmap(token),end=' ')
    print()  # This prints new line at the end of processing a line

