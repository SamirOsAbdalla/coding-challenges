# Link: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day_array = [0] * len(temperatures)
        cur_stack = []

        '''
        Main idea is to keep a stack of decreasing temps while continuously popping off elements of the stack
        while the current temp is > then the top element
        '''
        for i in range(len(temperatures)):
            if (len(cur_stack) == 0):
                cur_stack.append((temperatures[i], i))
            else:
                while (len(cur_stack) > 0 and temperatures[i] > cur_stack[-1][0]):
                    pop_temp, pop_index = cur_stack.pop()
                    day_array[pop_index] = i - pop_index
                cur_stack.append((temperatures[i], i))

        return day_array
