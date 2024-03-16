'''   
1. Two Sum  
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
'''

class Solution(object):
    def twoSum(self, nums, target):
        temp = []
        size = len(nums)

        for i in range(size):
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    temp.append(i)
                    temp.append(j)
                    return temp  

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print(result)  # Output: [0, 1]

