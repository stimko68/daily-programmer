"""
90 Degree 2D Array Rotate

Rotate a given an NxN sized 2D array of numbers by 90 degrees.

Example:
N = 3
Array:  1 2 3
        4 5 6
        7 8 9

Rotate: 7 4 1
        8 5 2
        9 6 3
"""
def rotate_array(array):
    return zip(*array[::-1])

if __name__ == "__main__":
    given = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],
        [0, 8, 6, 4, 2, 9, 7, 5, 3, 1],
        [0, 1, 2, 3, 4, 5, 4, 3, 2, 1],
        [9, 8, 7, 6, 5, 6, 7, 8, 9, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [9, 8, 7, 6, 7, 8, 9, 8, 7, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    r90 = rotate_array(given)
    r180 = rotate_array(r90)
    r270 = rotate_array(r180)

    print "======Rotated 90 Degrees====="
    for l in r90:
        print l

    print "\n======Rotated 180 Degrees====="
    for l in r180:
        print l

    print "\n======Rotated 270 Degrees====="
    for l in r270:
        print l