grades = [55, 67, 67, 88, 93, 97]
#micaela's solution:
#define a function
def find_largest(nums):
    p = nums
#or p = nums[0]
    for element in nums:
    if element > p:
        p = element
    return p

print find_largest(nums)
    
