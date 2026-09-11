class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for ch in strs:

            key = "".join(sorted(ch))

            if key not in anagram:
                anagram[key] = []

            anagram[key].append(ch)
        return list(anagram.values())