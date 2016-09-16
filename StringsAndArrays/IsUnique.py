"""
    Implement an algorithm to determine if a string has all unique characters.
    What if you can't use additional data structures?
"""

def IsUniqueHash( s ):
    list_of_chars = []
    for i in s:
        if i not in list_of_chars:
            list_of_chars.append(i)
        elif i in list_of_chars:
            return False
        else:
            print "Something went wrong in your conditional statements!"
    return True


def TestIsUniqueHash():
    if IsUniqueHash("abcde"):
        PassedTest(1)
    else:
        FailedTest(1)
    if not IsUniqueHash("aa"):
        PassedTest(2)
    else:
        FailedTest(2)


def PassedTest(test_number):
    print "Passed Test: ", test_number


def FailedTest(test_number):
    print "Failed Test: ", test_number


TestIsUniqueHash()


def IsUnique( s ):
    for i in range(len(s)):
        for x in range(len(s)):
            if (i != x and s[i] == s[x]):
                return False
    else:
        return True


print IsUnique("Cody")
print IsUnique("CC")