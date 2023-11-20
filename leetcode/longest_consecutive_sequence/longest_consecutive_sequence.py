# Problem link: https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0

        # remove duplicates
        cur_set = set(nums)
        for n in cur_set:
            # only get start of increasing sequence
            # sets in python use hashtables so this is O(1) lookup
            if (n-1 not in cur_set):
                length = 1
                while (n+length in cur_set):
                    length += 1
                output = max(output, length)
        return output
