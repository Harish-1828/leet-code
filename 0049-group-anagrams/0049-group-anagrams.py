class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            val=("").join(sorted(i))
            d[val].append(i)
        result=[]
        for i in d.values():
            result.append(i)
        return result 