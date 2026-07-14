class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=[]
        count=1
        max_count = 1
        if not nums:
            return 0
        for i in nums:
            if i not in unique:
                unique.append(i)
        
        unique.sort()
            
        for i in range(len(unique)-1):
            if unique[i+1]==unique[i]+1:
                count+=1
            else:
                max_count = max(max_count, count)
                count = 1

        max_count = max(max_count, count)
        return max_count



        
        

        