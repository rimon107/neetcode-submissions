class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = [] 
        
        
        for i in strs:
            flag = False
            for key, value in anagrams.items():
                if Counter(i) == value[0]:
                    value.append(i)
                    flag = True
                    break
            if flag == False:
                anagrams[i] = [Counter(i), i]
        
        for key, value in anagrams.items():
            result.append(value[1:])
        
        return result