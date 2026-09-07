class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lists={}
        for i in nums:
            if i not in lists:
                lists[i]=1
            else:
                lists[i]+=1

        sorted_lists=sorted(lists, key=lists.get,reverse=True)

        result=sorted_lists[:k]
      
        return result
        