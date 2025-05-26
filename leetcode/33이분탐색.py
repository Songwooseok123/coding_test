from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정렬된 경우
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 왼쪽으로
                else:
                    left = mid + 1   # 오른쪽으로

            # 오른쪽 절반이 정렬된 경우
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # 오른쪽으로
                else:
                    right = mid - 1  # 왼쪽으로

        return -1  # 못 찾은 경우
