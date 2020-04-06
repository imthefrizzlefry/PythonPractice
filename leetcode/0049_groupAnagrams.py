from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

if __name__ == "__main__":
    temp = Solution()

    print(temp.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
