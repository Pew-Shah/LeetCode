"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s= s.rstrip()

        l=s.split()

        return len(l[-1])

sol = Solution()
s= "hello world    "
print(sol.lengthOfLastWord(s))


"""
Alternative :

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j

sol = Solution()
s= "hello world    "
print(sol.lengthOfLastWord(s))

"""