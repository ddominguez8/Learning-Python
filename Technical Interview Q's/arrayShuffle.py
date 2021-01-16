# This problem was originally found from Leetcode
# The objective is that given an array and a midpoint,
# match up both sides of the array via the midpoint,
# basically in coordinate form.

# set up our return array
ret = []
# we can use the range 0 to n because we will increment the i and append, add that with n and we'll
# get the 'y' coordinate or the other half
        for i in range(0,n):
            ret.append(nums[i])
            ret.append(nums[i+n])
            # return ret array, which has the correct sequence of numbers
        return ret