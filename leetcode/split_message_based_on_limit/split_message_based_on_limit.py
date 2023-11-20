# Problem Link: https://leetcode.com/problems/split-message-based-on-limit/description/

# This problem was ROUGH. I could not understand the solution for the longest time.
# However, I eventually understood this brilliant solution I found in the solutions tab.
# I changed some variable names and added some comments to hopefully make the solution easier to understand.
class Solution:

    def splitMessage(self, s: str, limit: int) -> List[str]:
        message_size = len(s)

        # < / > has length 3
        default_suffix_length = 3

        # The b-value in <a/b>
        num_splits = 0

        current_line = 0
        # We have two loop conditions A and B. A is to make sure the longest suffix length which is <num_splits/num_splits>
        # i.e. the last suffix satisfies the line limit. Now for condition B. The left-side of B computes the total number of
        # characters NEEDED to split the message across num_splits lines. The right side computes the total number of characters
        # we CAN USE in this message including all suffix lengths given the current num_splits. All current_line does is keep track all cumulative a's in <a/num_splits>
        # until we reach the correct num_splits. As long as the the number needed exceeds the number we can use we must keep increasing the number of lines in the message
        while default_suffix_length + len(str(num_splits)) * 2 <= limit and current_line + message_size + (3 + len(str(num_splits))) * num_splits > limit * num_splits:
            num_splits += 1
            current_line += len(str(num_splits))
        res = []

        # This variable will keep track of the current char starting position in our message string
        cur_message_index = 0

        num_splits_length = len(str(num_splits))

        # Only if we left the previous loop due to condition B being false will we actually have a valid num_splits value
        if default_suffix_length + len(str(num_splits)) * 2 <= limit:
            # The string is formated as main_string<a/b>
            for cur_a in range(1, num_splits + 1):

                # l denotes the number of message string characters we need to obtain relative from cur_message_index
                l = limit - (len(str(cur_a)) +
                             default_suffix_length + num_splits_length)
                res.append("{main_string}<{a}/{b}>".format(
                    main_string=s[cur_message_index:cur_message_index + l], a=cur_a, b=num_splits))
                cur_message_index += l
        return res
