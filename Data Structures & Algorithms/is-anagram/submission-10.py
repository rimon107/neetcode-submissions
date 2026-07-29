from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        if len(s) == len(t):
            for a in s:
                dict_s[a] = dict_s[a] + 1
            
            for b in t:
                dict_t[b] = dict_t[b] + 1
            
            return dict_s == dict_t

        return False
        