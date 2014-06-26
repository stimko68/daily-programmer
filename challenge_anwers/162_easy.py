"""
Reads from two files, one containing a list of words, and
another containing an encoded string. The script should
decode each string and print out the corresponding words
from the first file. Decoding rules:

 - If the chunk is a number (e.g., 37), print the corresponding
   word
 - If the chunk is followed by a caret (e.g., 37^) then the word
   should be capitalized (e.g., Ball)
 - If the chunk is followed by a bang (e.g., 37!) then the word
   should be all caps (e.g., BALL)
 - If the chunk is a hyphen, print the hyphen instead of a space
   character
 - If the chunk is any of the following symbols: . , ? ! ; : then
   print the chunk at the end of the previous word
 - If the chunk is an R (upper or lowercase) then print a newline
 - If the chunk is an E (upper or lowercase) then the end of the
   input has been reached
"""
import re
import sys

dict = {}
word_list = []
strings_to_decode = []

with open('162_easy.txt', 'r') as source_words:
    for word in source_words:
        word_list.append(word.rstrip())
    for i in range(len(word_list)):
        dict[i] = word_list[i]

with open('162_easy_encoded.txt', 'r') as encoded_strings:
    for string in encoded_strings:
        strings_to_decode.append(string.split(' '))
    for element in strings_to_decode:
        element[-1] = element[-1].strip()

for sublist in strings_to_decode:
    answer = ""
    newline = "\n"
    for i in sublist:
        if re.match(("^([0-9]\^|[1-9][0-9]\^)"), i) is not None:
            first_caps_word = dict[int(i.replace("^", ""))]
            sys.stdout.write(first_caps_word.capitalize() + " ")
        elif re.match(("^([0-9]\!|[1-9][0-9]\!)"), i) is not None:
            all_caps_word = dict[int(i.replace("!", ""))]
            sys.stdout.write(all_caps_word.upper() + " ")
        elif re.match(("^([0-9]|[1-9][0-9])"), i) is not None:
            sys.stdout.write(dict[int(i)] + " ")
        elif re.match(("^([\.,\?\!;:-])"), i) is not None:
            sys.stdout.write(i)
        elif re.match(("^([R-r][E-e])"), i) is not None:
            print("\n")