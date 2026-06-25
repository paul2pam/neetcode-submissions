class Solution:
    def trap(self, height: List[int]) -> int:
        
        from_left = [0] * len(height)
        from_right = [0] * len(height)

        curr = 0
        i = 0
        while(i < len(height)):
            from_left[i] = max(curr - height[i], 0)
            curr = max(height[i], curr)
            i += 1

        j = len(height) - 1
        curr = 0

        while (j >= 0):
            from_right[j] = max(curr - height[j], 0)
            curr = max(height[j], curr)
            j -= 1
        
        res = 0
        for i in range(len(from_left)):
            res += min(from_left[i], from_right[i])
        return res
        

