class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashs={}

        stores={}

        if len(s)!=len(t):
            return False

        for i in s:
            if i not in hashs:
                hashs[i]=1
            else:
                hashs[i]+=1

        for j in t:
            if j not in stores:
                stores[j]=1
            else:
                stores[j]+=1

        if hashs==stores:
            return True

        return False
