'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# intution
'''
1 1 1 3 3 4 3 2 4 2

for the above example we just have to tell if there are any duplicate value present

so to find the duplication of value the best data sturcture is hashset
'''

def containsDuplicate(nums) -> bool:
    hashset = set()
    
    for ele in nums:
        if ele in hashset:
            return True
        hashset.add(ele)
    
    return False
                