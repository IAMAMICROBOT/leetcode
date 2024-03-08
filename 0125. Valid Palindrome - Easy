class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                if i.isupper():
                    s1+=i.lower()
                else:
                    s1+=i
        return s1==s1[::-1]
