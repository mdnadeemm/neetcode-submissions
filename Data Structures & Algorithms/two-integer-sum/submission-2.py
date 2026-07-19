class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        diary = {}

        for idx,item in enumerate(nums):
            difference = target - item;
            if difference in diary:
                return [diary[difference], idx]
            diary[item] = idx

        return []


            