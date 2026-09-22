class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash={}

        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1

        sorted_list=sorted(hash,key=hash.get,reverse=True)

        return sorted_list[:k]

        
        
        