class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        condict={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        try:
            i=0
            while (i< len(s)):
                if(s[i]+s[i+1]in condict):
                    res+=condict[(s[i]+s[i+1])]
                    i+=1
                else:
                    res+=condict[s[i]]
                i=i+1
        finally:
            if i<len(s):
                res+=condict[s[i]]
            return res
                
