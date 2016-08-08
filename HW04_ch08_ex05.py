# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_word(word,n):
    word = word.lower()
    encrypt = ''
    offset = 96 # starting index for letters
    for letter in word:

        # print('letter:')
        # print(ord(letter) - offset) # testing
        alpha = (ord(letter) - offset + n) % 26
        # print('crypt:') # test
        # print(alpha)
        encrypt = encrypt + chr(alpha + offset)

    return encrypt


###############################################################################
def main():

    print(rotate_word('hal',+20))
    print(rotate_word('zzz',+3)) # upper-bound test 'ccc'
    print(rotate_word('aaa',-3)) # lower_bound test 'xxx'
    print(rotate_word('aaa',+26)) # full rotation test
    print(rotate_word('cheer',7)) # full rotation test
    print(rotate_word('Melon',-10)) # full rotation test


if __name__ == '__main__':
    main()
