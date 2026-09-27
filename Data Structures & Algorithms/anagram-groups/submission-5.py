class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in dictt:
                dictt[key]=[i]
            else:
                dictt[key].append(i)

        answer=list(dictt.values())

        return answer





        