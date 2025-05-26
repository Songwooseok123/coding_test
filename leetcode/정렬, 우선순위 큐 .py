class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop

        z = []
        cc = 0
        for i in nums:
            heappush(z,i)
            cc +=1
            if cc >k:
                heappop(z)
        return z[0]
