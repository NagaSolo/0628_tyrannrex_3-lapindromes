"""Input:
        First line of input contains a single integer T, the number of test cases.
        Each test is a single line containing a string S composed of only lowercase English alphabet.

    Output:
        For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
        
    Constraints:
        1 ≤ T ≤ 100
        2 ≤ |S| ≤ 1000, where |S| denotes the length of S
"""
test_string = 'abcdcba'
string_length = len(test_string)
print (string_length)
# using string comprehension; split the string
part_one = test_string[0:string_length//2 if string_length%2 == 0 else ((string_length//2) + 1)]
part_two = test_string[string_length//2:]
print(part_one)
print(part_two)

# T = int(input())
# while T>=1 & T<=100:
#     if input_string == palindrome:
#         print('YES')
#     else:
#         print('NO')