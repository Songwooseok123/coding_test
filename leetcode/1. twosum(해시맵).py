class Solution:
    # hash_map
    시간복잡도 n , 공간 복잡도 n 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,i_v in enumerate(nums):
            remain = target - i_v
            if remain in hash_map:
                return [hash_map[remain], i]
            hash_map[i_v] = i
  
  
