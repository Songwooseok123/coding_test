class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 부분합의 최댓값이 최소가 되도록

        s = min(nums)
        e = sum(nums)
        answer = None

        def get_partition_num(mid):
            part_sum = 0
            cc = 1
            if mid < max(nums):
                return 1e9 
            for i in nums:
                if part_sum+i > mid:
                    part_sum = i
                    cc +=1
                else:
                    part_sum +=i
            return cc 


        while s<=e:
            mid = (s+e)//2
            needed_partition = get_partition_num(mid)
            if needed_partition > k:
                s = mid+1
            else:
                e = mid-1
                answer = mid
            print(s,e,mid)
        return answer 

        
