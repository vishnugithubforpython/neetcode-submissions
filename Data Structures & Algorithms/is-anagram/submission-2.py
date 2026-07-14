class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        hash={}
        hashs={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        for j in t:
            if j not in hashs:
                hashs[j]=1
            else:
                hashs[j]+=1
        
        if hash == hashs:
            return True
        else:
            return False





        