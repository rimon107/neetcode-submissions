class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for i in strs:
            c = [0] * 26

            for a in i:
                c[ord(a) - ord("a")] += 1
            
            result[tuple(c)].append(i)

        return list(result.values())