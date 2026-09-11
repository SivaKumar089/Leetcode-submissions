class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {"}":"{",")":"(","]":"["}
        stack = []

        for char in s:

            if char in hash_map:
                top_element = stack.pop() if stack else '#'

                if top_element != hash_map[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
