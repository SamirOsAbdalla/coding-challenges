from collections import deque

## Link: https://leetcode.com/problems/sliding-window-maximum/description/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        res = []

        ## Here we use a deque due to the way we will be storing the values in a given window. The deque will store window values
        ## in decreasing order with new values continuously removing elements of the deque from the right so long as the new value
        ## is larger. This is because if a new value is greater than all previous values in a window,
        ## then because the new value appears at the end  
        ## of the window it will ALWAYS be the current value to consider. For example if we have 5 -1 2 4 and the window size is 3 the
        ## deque will be 5 then 5 -1 then 5 2. -1 will never be the max value in the current window since 2 is there so we need not 
        ## consider it anymore. From there, the current window maximum is simply the top of the deque.
        queue = deque(res)

        ## This code is to set up the deque with the first window
        for i in range(r):
            if(len(queue) == 0):
                queue.appendleft(nums[i])
            elif(nums[i] > queue[-1]):
                while(len(queue) > 0 and nums[i] > queue[-1]):
                    queue.pop()
                queue.append(nums[i])
            else:
                queue.append(nums[i])
        res.append(queue[0])

        while(r < len(nums)):

            ## We remove the element at l at the beginning of each iteration. If it was the max value then
            ## we now need to consider other values in the window. However if it wasn't the previous window maximum,
            ## it would have been popped from the queue by a larger element since it came before the larger element.
            if(nums[l] == queue[0]):
                queue.popleft()  
            l+=1
            if(len(queue) == 0):
                queue.appendleft(nums[r])
            elif(nums[r] > queue[-1]):
                while(len(queue) > 0 and nums[r] > queue[-1]):
                    queue.pop()
                queue.append(nums[r])
            else:
                queue.append(nums[r])
            res.append(queue[0])
            r+=1
        return res

        

        
