"""Input:
        First line of input contains a single integer T, the number of test cases.
        Each test is a single line containing a string S composed of only lowercase English alphabet.

    Output:
        For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
        
    Constraints:
        1 ≤ T ≤ 100
        2 ≤ |S| ≤ 1000, where |S| denotes the length of S
"""

"""Splitting the string"""
# test_string = 'abcdcba'
# string_length = len(test_string)
# print (string_length)
# # using string comprehension; split the string, handle if length is an odd number
# part_one = test_string[0:string_length//2 if string_length%2 == 0 else ((string_length//2) + 1)]
# part_two = test_string[string_length//2:]
# print(part_one)
# print(part_two)

"""experimenting with sorted method"""
# print(sorted(part_one))
# print(sorted(part_two))

"""Using Standard input of Python 3
    variables are based on CodeChef palindrome question
"""

T = range(1, 100)
std_input = int(input())
if std_input in T:
    for looping_program in range(std_input):
        S = range(2, 1000)
        string_input = input()
        string_input_length = len(string_input)
        if string_input_length in S:
            part_one = string_input[0:string_input_length//2 if string_input_length%2 == 0 else ((string_input_length//2) + 1)]
            part_two = string_input[string_input_length//2:]
            if sorted(part_one) == sorted(part_two):
                # using string comprehension; split the string, handle if length is an odd number
                print('YES')
            else:
                print('NO')
        else:
            break