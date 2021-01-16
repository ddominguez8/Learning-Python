# This problem was originally found off Leetcode
# a friend of mine recommended to learn how to combat
# these problems using Python, so that's what I'll do
# This problem originally worked on 12/31/2020

nums = [1, 2, 3, 4, 5]
sum=[nums[0]]
for i in range (1,len(nums)):
    sum.append(sum[i-1]+nums[i])
