class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs={}
        was={}
       
        if len(s)!=len(t):
            return  False
        for i in s:
            if i not in hashs:
                hashs[i]=1
            else:
                hashs[i]+=1
        for j in t:
            if j not in was:
                was[j]=1
            else:
                was[j]+=1
        
        if hashs == was:
            return True
        return False
                
     





        