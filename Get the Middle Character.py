"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
 return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an
 error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry
  about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
"""


def get_middle(s):
    user_string_len = len(s)
    user_string_arr = [letter for letter in s]
    if user_string_len % 2 != 0:
        user_string_len -= 1
        user_string_len = user_string_len / 2

        return print(user_string_arr[int(user_string_len)])

    elif user_string_len == 1:
        return print(s)

    else:
        user_string_len = user_string_len / 2
        output = user_string_arr[int(user_string_len) - 1] + user_string_arr[int(user_string_len)]

        return print(output)


get_middle('middle')
