class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {k: v for v, k in enumerate(nums)}
        for i in range(len(nums)):
            hash_target = target - nums[i]
            if hash_target in num_hash:
                j = num_hash[hash_target]
                if i == j:
                    continue
                return[i,j]
