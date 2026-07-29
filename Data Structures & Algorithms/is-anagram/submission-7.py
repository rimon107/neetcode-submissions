class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()

        if len(s) == len(t):
            for a in s:
                dict_s[a] = dict_s.get(a, 0) + 1
            
            for b in t:
                dict_t[b] = dict_t.get(b, 0) + 1
            
            return dict_s == dict_t

        return False
        