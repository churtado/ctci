"""
# Is Unique: implement an algorithm to determine if a string has all unique characters.
What is you cannot use additional data structures?
"""

"""
First Implementation

First ask, is the string ASCII or Unicode? We'll assume ASCII. If not we'd need to increase storage size.
Of course all this assumes I'm using something like c where strings are arrays where memory is allocated
statically. 

ASCII contains 128 characters. We create an array of 128 booleans and flag as true the characters that are
in the string. In a c-language this can take advantage of a char being a byte. But in python we would create
a hash to make the code more understandable.

Here we'll assume a simple alphabet that has only a and b. If it was ASCII it would be 128, and unicode 256.

Complexity in time: O(n) where n = length of string
You could argue time is O(1) because it will never iterate more than the length of the alphabet.
If the algorithm is changed to be able to accept different sized alphabets, then the complexity would be:
O(min(c, s)) where c = length of alphabet, s = length of string
Complexity in space: O(1), alphabet size is constant.
"""
def isUnique(s: str) -> bool:
    length_alphabet = 2
    if len(s) > length_alphabet:
        # the string has at least 1 of every character and so is not unique
        return False
    char_set = {'a': False, 'b': False}
    for c in s:
        if char_set[c]:
            return False
        else:
            char_set[c] = True
    return True

print(isUnique('a'))
print(isUnique('b'))
print(isUnique(''))
print(isUnique('ab'))
print(isUnique('aa'))
print(isUnique('bb'))

"""
Implementation using a bit vector
essentially we'd have an int with as many bits as there are characters
then we'd assign a bit to each character based on a position in the bit.
So for example a=1st bit (least significant), b= second bit, etc.
The int is initialized at 0, and the bits are marked. In order to do this
in python though, you'd need to get a way to get ASCII codes to get the
character's position. So, a=100, b=101, etc. for example.
"""

"""
Implementation using no additional data structures
Complexity in time: O(n) where n = length of string
Complexity in space: O(1)
"""
def isUniqueNoHash(s: str) -> bool:
    sorted_s = sorted(s)
    for i in range(1, len(s)):
        if sorted_s[i-1] == sorted_s[i]:
            return False
    return True
print('======== No hash ========')
print(isUniqueNoHash('a'))
print(isUniqueNoHash('b'))
print(isUniqueNoHash(''))
print(isUniqueNoHash('ab'))
print(isUniqueNoHash('aa'))
print(isUniqueNoHash('bb'))

"""
Implementation using no additional data structures
and without modifying the array.
Complexity in time: 
Complexity in space: 
"""
def isUniqueNoHashPure(s: str) -> bool:

    return True
print('======== No hash pure ========')
print(isUniqueNoHashPure('a'))
print(isUniqueNoHashPure('b'))
print(isUniqueNoHashPure(''))
print(isUniqueNoHashPure('ab'))
print(isUniqueNoHashPure('aa'))
print(isUniqueNoHashPure('bb'))