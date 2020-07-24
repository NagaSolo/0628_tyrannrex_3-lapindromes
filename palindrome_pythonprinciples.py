''' Challenge Palindrome

    A string is a palindrome when it is the same when read backwards.

    For example, the string "bob" is a palindrome. So is "abba". 
    But the string "abcd" is not a palindrome, because "abcd" != "dcba".

    Write a function named palindrome that takes a single string as its parameter. 
    Your function should return True if the string is a palindrome, and False otherwise.

'''
# procedural
def palindrome(a_string):
    length = len(a_string)
    if (length % 2 == 0):
        a_string1 = sorted(a_string[:(length//2)])
        a_string2 = sorted(a_string[length//2:])
        if a_string1 == a_string2:
            return True
        else:
            return False
    else:
        a_string1 = sorted(a_string[:(length//2)+1])
        a_string2 = sorted(a_string[length//2:])
        if a_string1 == a_string2:
            return True
        else:
            return False

# driver
if __name__ == '__main__':
    string_input = input()
    print(palindrome(string_input))