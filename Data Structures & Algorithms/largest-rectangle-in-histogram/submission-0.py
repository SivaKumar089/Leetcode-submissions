class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.nse(heights, n)
        pse = self.pse(heights, n)
        max_area = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width

            max_area = max(max_area, area)
        return max_area

    def pse(self, heights, n):
        stack = []
        pse = [-1] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse

    def nse(self, heights, n):
        stack = []
        nse = [-1] * n

        for i in range(n - 1, - 1, - 1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse 