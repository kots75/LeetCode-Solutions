#brute force solution that is O(n^2) time complexity
# def twoSum(nums, target):
#     for i in range(len(nums)):
#       for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#           return [i, j]
        
#Optimal one pass solution that is O(n) time complexity using hashmap
def twoSum(nums, target):
    prevMap = {} # num : index

    for i, num in enumerate(nums):
      diff = target - num
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[num] = i
    return

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))