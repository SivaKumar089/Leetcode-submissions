class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:

            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if ch == "+":
                    stack.append(num2 + num1)
                elif ch == "-":
                    stack.append(num2 - num1)
                elif ch == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
        return stack[-1]
