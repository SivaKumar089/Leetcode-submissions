class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_set = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in char_set:
                char_set[key] = []

            char_set[key].append(word)
        return list(char_set.values())