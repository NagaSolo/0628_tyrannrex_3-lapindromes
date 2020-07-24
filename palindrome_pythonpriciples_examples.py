# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.
def palindrome_method1(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# recursive solution: equivalent to the above.
def palindrome_method2(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome_method2(string[1:-1])

# smarter solution:
# check if reversing the string gives the same string.
def palindrome_method3(string):
    return string == string[::-1]