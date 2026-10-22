class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'}':'{', ']':'[', ')':'('}
        stack = []
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            else:
                top_element = stack.pop() if stack else '#'

                if top_element != hash_map[ch]:
                    return False
        return len(stack) == 0
