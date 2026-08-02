class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        count = 0
        n = len(temperatures)

        for i in range(n):
            x = temperatures[i]
            if i+1 < n:
                flag = False
                for temp in temperatures[i+1:]:
                    count += 1
                    if temp > x:
                        flag = True
                        break
            if flag == True:
                result.append(count)
            else:
                result.append(0)
                
            count = 0
        
        return result
