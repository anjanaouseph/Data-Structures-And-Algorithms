class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #using the array as set itself

        result = []

        for i in range(len(nums)):
            idx = abs(nums[i])-1 #the no.s actual index in the array from 1 to N, 4 will be 3
            #1 will be 0 and so on.
            if nums[idx] > 0:
                nums[idx] *= -1 #mark the number at that idx negative
            
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)

        return result