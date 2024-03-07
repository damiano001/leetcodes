'''
88. Merge Sorted Array
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        i = 0
        j = 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        while i < m:
            temp.append(nums1[i])
            i += 1
        
        while j < n:
            temp.append(nums2[j])
            j += 1 
        
        nums1[:] = temp

nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6] 
n = 3

solution = Solution()  
solution.merge(nums1, m, nums2, n) 

print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

