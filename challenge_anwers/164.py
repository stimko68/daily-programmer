
# Print an array containing numbers that
# are evenly divisible by 3 or 5
def number_array():
    output = []
    for i in range(100):
        if i % 3 == 0 & i % 5 == 0:
            output.append(i)

    print output

# Verifies if given word is an anagram of
# another
def anagram_verify(given, test):
    if given[::-1] == test:
        print("The words are anagrams!")
    else:
        print("Not an anagram")

# Removes a given letter from a given word
import re
def remove_letter(word, letter):
    if re.search(letter, word):
        print word.replace(letter, "")
    else:
        print("Word doesn't contain given letter.")

# Sums all elements in an array
def sum_array(array):
    output = 0
    for n in array:
        output += n
    print(output)

# Performs a bubble sort on a given array
def bubble_sort(array):
    array_length = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for n in range(array_length):
            if array[n] > array[n+1]:
                sorted = False
                array[n], array[n+1] = array[n+1], array[n]
    print array