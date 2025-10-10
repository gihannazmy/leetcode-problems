




# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        valid_triple = []
        
        if len(nums) < 3:
            return False
        for num in nums:
            if not valid_triple:
                valid_triple.append(num)
            elif len(valid_triple) == 1:
                if num > valid_triple[0]:
                    valid_triple.append(num)
                else:
                    valid_triple[0] = num 
            elif len(valid_triple) == 2:
                if num > valid_triple[1]:
                    return True  
                elif num > valid_triple[0] and num < valid_triple[1]:
                    valid_triple[1] = num 
                elif num < valid_triple[0]:
                    valid_triple[0] = num
        return False
