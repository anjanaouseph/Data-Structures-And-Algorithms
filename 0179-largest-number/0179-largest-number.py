from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #edge case if 0000 -> we should only return 0
            #Brute force approach? Try all possible permutations of the numbers and pick the    maximum formed number. Total: O(n! * n) -> extra n for concatenation. Generate all permutations of the array.
    # For each permutation:
    # Convert numbers to strings
    # Concatenate them
    # Convert the result to a number (or compare as strings)
    # Track the maximum
    #optimal soln is using greedy. First sort and then find local maximum no between the two which will give the largest sum as output. Before comparing u can convert it to a string. place them in the order that gives a bigger concatenation. Whichever is larger determines the order.

        for i,val in enumerate(nums):
            nums[i] = str(val) #convert to string

        def compare(a, b):
            if a+b > b+a:
                return -1 #put a before b
            else:
                return 1 #put b before a. even if they are equal return 1 in this case. #generally we shud return 0
        nums = sorted(nums, key = cmp_to_key(compare)) #This is using timesort so nlogn

        return str(int("".join(nums))) #convert result to int to remving leading zeroes automatically, then convert back to string.

#if we keep as integers and compare then? 3+30 and 30+3 gives same result. but we want 3 to be before as "3"+"30" gives "330" but other way is "303" so "330" is the largest here.
# This is greedy because for every pair we Pick the order that gives the bigger result which eventually leads to the biggest no to return.
# For every pair of numbers, we choose the order that produces the larger concatenation, and these local optimal choices lead to the globally largest number.
# TC: O(nlogn*2k+n), k is for string appending. a+b, largest digit possible is 10 raised to 9 so k will be 10*2
# SC: O(n)

