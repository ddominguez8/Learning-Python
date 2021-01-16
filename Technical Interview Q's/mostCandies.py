# This problem was originally found off Leetcode
# The objective is, given a certain n,
# added onto any of the elements within the list,
# will they become or be equivalent to the max in the array
# return true or false
# Worked on 1/16/2021

# this was only an example case I worked on
candies = [2, 3, 5, 1, 3]
extraCandies = 3
ret = []

# Find the max value of the list
richKid = max(candies)
for i in candies:
    # Used a tempVar so that I could add up an element of the list
    # along with the extra candies so that it would equate or be more than
    # the max
    tempVar = i + extraCandies
    # append true or false depending on the result
    if tempVar >= richKid:
        ret.append(True)
    else:
        ret.append(False)

# for i in range(len(ret)):
#     print(bool(i))