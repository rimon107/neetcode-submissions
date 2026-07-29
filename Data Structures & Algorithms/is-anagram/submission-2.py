class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()

        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
                 s_dict[x] = 0
        
        for x in t:
            if x in t_dict:
                t_dict[x] += 1
            else:
                 t_dict[x] = 0

        if s_dict == t_dict:
            return True
        return False