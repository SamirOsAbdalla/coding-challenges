#Link: https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ## t can't be a substring of s if t is larger 
        if(t == "" or len(t) > len(s)):
            return ""

        ## these dictionaries will store the frequency of characters in a given window (the entire length for t in this case)
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        ## res will keep track of the current, smallest range of indices that satisfy the conditions
        ## reslen is a QOL variable that makes comparing the current range in a given iteration to the
        ## current smallest range easier
        res, resLen = [-1,-1], float("infinity")

        ## these variables will help with determining whether or not our current window has the necessary frequency of characters
        ## that match the frequency of characters in t
        have, need = 0, len(countT)


        l = 0
        for r in range(len(s)):
            c = s[r]

            ## increase the frequency of the current character we are at in s
            window[c] = 1 +window.get(c,0)

            ## have only increases once the frequency of a character in a given window in s matches the frequency of the same character
            ## in t
            if(c in countT and window[c] == countT[c]):
                have+=1

            ## Since a given window can look like XXXXOOX where X's are characters that don't contribute to the "haves" 
            ## and O's are haves, there is a lot of "fluff" at the beginning of the window. The variable l will keep increasing
            ## until we reach and decrease the frequency of a character that appeared in t AND by decreasing that frequency,
            ## we would now need another character of that type in order to contain all of t in that window. The second check is for
            ## the case that if we have 4 B's in a given window in s and t only has three B's then removing the first B still satisfies
            ## that we have all the B's in t.
            while(have == need):
                if(r-l+1 < resLen):
                    resLen = r-l+1
                    res = [l, r]
                window[s[l]] -= 1
                if(s[l] in countT and window[s[l]] < countT[s[l]]):
                    have-=1
                l+=1
            
        l, r = res

        ##if resLen never got updated then there was no valid window
        if(resLen != float("infinity")):
            return s[l:r+1]
        return ""

        
