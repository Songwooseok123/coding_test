class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 1. 시작점 기준 정렬
        intervals.sort(key=lambda x: x[0])
        
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                # 겹치지 않으면 새로운 구간 시작
                merged.append(interval)
            else:
                # 겹치면 병합
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
 


        
