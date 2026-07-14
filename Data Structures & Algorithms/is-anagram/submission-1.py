class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}
        lists={}
        if len(s)!= len(t):
            return False
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        for j in t:
            if j not in lists:
                lists[j]=1
            else:
                lists[j]+=1
        if hash == lists:
            return True
        else:
            return False               
