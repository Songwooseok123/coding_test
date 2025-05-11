class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            # mid가 짝수인지 홀수인지에 따라 짝 검사 위치 조정
            if mid % 2 == 1:
                mid -= 1  # 항상 짝수 인덱스로 맞추기
            
            if nums[mid] == nums[mid + 1]:
                # 정상이면 오른쪽으로 탐색
                left = mid + 2
            else:
                # 깨졌으면 왼쪽으로 탐색
                right = mid
        
        return nums[left]
        