class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_index={}
        for i in nums:
            if i in num_index:
                num_index[i] += 1

            else :
                num_index[i] = 1

        result=[]
        while k > 0:
            largest_value = 0
            large_value_key = None
            for key, value in num_index.items():
                if value >= largest_value:
                    largest_value = value
                    large_value_key = key
            result.append(large_value_key)
            num_index.pop(large_value_key)
        
            k -= 1
        return result