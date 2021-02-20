class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr = 0
        rptr = (len(height)-1)
        maxarea = min(height[lptr], height[rptr]) * rptr
        while lptr < rptr:
            if height[lptr] < height[rptr]:
                maxarea = max(maxarea, min(height[lptr], height[rptr]) * (rptr-lptr))
                lptr = lptr+ 1
            elif height[lptr] >= height[rptr]:
                maxarea = max(maxarea, min(height[lptr], height[rptr]) * (rptr-lptr))
                rptr = rptr-1
        return maxarea
            
        