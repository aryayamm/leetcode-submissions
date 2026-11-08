class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            selisih = target-nums[i]
            if selisih in map:
                return [map[selisih], i]
            map[nums[i]] = i

        