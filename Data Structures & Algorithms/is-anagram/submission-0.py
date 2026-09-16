class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm1={}
        for i in range(len(s)):
            hm1[s[i]]= 1+ hm1.get(s[i],0)
        for j in range(len(t)):
            if t[j] in hm1:
                hm1[t[j]]-=1
                if hm1[t[j]]==0:
                    hm1.pop(t[j])
            else:
                return False
        return len(hm1)==0