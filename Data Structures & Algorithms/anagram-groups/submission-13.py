from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a to z for each string, represents map
            for char in s:
                count[ord(char) - ord('a')] += 1

            groupDict[tuple(count)].append(s)

        return list(groupDict.values())

                    