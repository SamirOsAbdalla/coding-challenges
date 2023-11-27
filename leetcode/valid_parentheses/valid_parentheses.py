# Problem Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # The algorithm is simply: if c is an opening bracket, push it on the stack
        # If c is a closing bracket check the top of the stack for its corresponding
        # opening bracket
        for c in s:
            if (c == "(" or c == "[" or c == "{"):
                stack.append(c)
            elif (c == ")"):
                if (len(stack) == 0 or stack[-1] != "("):
                    return False
                stack.pop()
            elif (c == "]"):
                if (len(stack) == 0 or stack[-1] != "["):
                    return False
                stack.pop()
            elif (c == "}"):
                if (len(stack) == 0 or stack[-1] != "{"):
                    return False
                stack.pop()
        # This accounts for the scenario like s = "[" or s ="(){" where we are left with a straggler
        # at the end
        if (len(stack) == 0):
            return True
        return False
