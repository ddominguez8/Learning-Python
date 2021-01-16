# This problem was originally found off Leetcode
# This problem originally worked on 1/16/2020

# We init a maxNumber var to finalize our answer
maxNumber = 0
# Iterate through the entire 2D array
for x in accounts:
    # We can use the max and sum function to 1. sum up each array and
    # 2. compare to see if it is larger than our previous max
    maxNumber = max(maxNumber, sum(x))
# Return our final answer after the loop is finished
return maxNumber
