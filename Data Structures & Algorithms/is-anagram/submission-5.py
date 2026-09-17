class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False
        hashs={}
        washs={}
        for i in s:
            if i not in hashs:
                hashs[i]=1
            else:
                hashs[i]+=1
        for j in t:
            if j not in washs:
                washs[j]=1
            else:
                washs[j]+=1

        if hashs == washs:
            return True
        else:
            return False
        


        