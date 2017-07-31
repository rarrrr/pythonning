#grades = [55, 67, 67, 88, 93, 97]
#micaela's solution:
#define a function
#def find_largest(nums):
#    p = nums
#or p = nums[0]
#    for element in nums:
#    if element > p:
#        p = element
#    return p

#print find_largest(nums)

grades = [67, 55, 97, 88, 93, 67]
grades.sort();

bottom = grades[0]
top = grades[-1]

print "bottom is", bottom
print "top is", top
