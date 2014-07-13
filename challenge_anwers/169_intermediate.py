"""
Home Row Spell Check

Given a string that may have mistyped characters, do a "spell check"
given the user inputting the string is using a QWERTY keyboard. The
mistyped words will be shifted by one or two characters from the actual
word.

Example

Input:  The quick ntpem fox jumped over rgw lazy dog.
Output: The quick {brown} fox jumped over {the} lazy dog.
"""
with open('169_int.txt', 'r+') as f:
    valid_words = []
    for line in f:
        valid_words.append(line.rstrip())

test_string = "The quick ntpem fox jumped over rgw lazy dog."
input_text = test_string.split()
result = []
keyboard = [list("qwertyuiop"), list("asdfghjkl"), list("zxcvbnm")]

for word in input_text:
    if word in valid_words:
        result.append(word)
    else:
       checker = list(word)
