from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for s in strs:
            count = Counter(s)

            groupDict[tuple(sorted(count.items()))].append(s)

        return list(groupDict.values())
            