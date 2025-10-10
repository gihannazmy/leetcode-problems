
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = []
        vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        for liter in s:
        
            if liter in vowels:
                vowel_list.append(liter)
        vowel_list.reverse()
        reversed_vowles_word = []
        for liter in s:
        
            if liter in vowels:
                vowel = vowel_list.pop(0)
                reversed_vowles_word.append(vowel)


            else:
                reversed_vowles_word.append(liter)

        return ''.join(reversed_vowles_word)