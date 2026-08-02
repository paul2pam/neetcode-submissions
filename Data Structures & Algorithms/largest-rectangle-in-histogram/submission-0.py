class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initialize the stack with the 0-indexed bar in the histogram
        # if the bar is taller than previous, we add our current height and index to the stack
        # if the current bar is shorter or equal, we pop until the top item in the stack is <= height our new bar, then add our current height and the index of the last item we popped
        #each time we pop from the rectangle, compute res = max(area, res)
        #at the end, we're going to loop through the stack once more

        stack = []
        stack.append((0, -1))

        res = 0

        for i in range(len(heights)):
            if heights[i] > stack[-1][0]:
                stack.append((heights[i], i))
            else: 
                last_i = stack[-1][1] #0
                while stack and heights[i] <= stack[-1][0]:
                    last_height, last_i = stack.pop() #7, 0
                    area = (i - last_i) * last_height
                    res = max(area, res)
                stack.append((heights[i], last_i))
        #print(stack, res)
        while stack:
            area = (len(heights) - stack[-1][1]) * stack[-1][0]
            res = max(area, res)
            stack = stack[:-1]
        
        return res
                    