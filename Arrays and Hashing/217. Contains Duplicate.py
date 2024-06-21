#the solutuion i came up with myself that works ok
# def containsDuplicate(nums):
#     myDict = {}

#     for n in nums:
#       if n in myDict:
#         myDict[n] += 1
#       else:
#         myDict[n] = 1
      
#     print(myDict)
#     for val in myDict.values():
#       if val > 1:
#         return True
#     return False

#more concise and easier solution using sets instead of dictionaries
def containsDuplicate(nums):
    dupes = set()
    for n in nums:
        if n in dupes: 
            return True
        dupes.add(n)
    return False

nums = [2,14,18,22,22]
print(containsDuplicate(nums))