class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        indices = []
        
        for i, t in enumerate(temperatures):
            if not indices:
                indices.append(i)
                continue
            
            while indices and temperatures[indices[-1]] < t:
                answer[indices[-1]] = i - indices[-1]
                indices.pop()
            
            indices.append(i)
        
        return answer