'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

Input: nums = [1,2,3]
Output: [1,3,2]
'''

def nextPermutation(nums):
    
    def reverse(L, start, end):
        while start < end:
            L[start], L[end] = L[end], L[start]
            start, end = start + 1, end - 1
            
    i = len(nums) - 1
    n = len(nums)
    
    while i >= 1 and nums[i] <= nums[i - 1]:
        i -= 1
        
    if i != 0:
        j = i
        while j + 1 < n and nums[j + 1] > nums[i - 1]:
            j += 1
        
        nums[i-1], nums[j] = nums[j], nums[i - 1]
    
    reverse(nums, i, n - 1)

nums = [1,2,3]
nextPermutation(nums)
print(nums)
