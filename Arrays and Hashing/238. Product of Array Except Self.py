#solution using separate prefix and postfix arrays to store the product of all elements before and after the current element
def productExceptSelf(nums):
  n = len(nums)
  res = []
  prefix = [1] * n
  postfix = [1] * n

  for i in range(1,n):
    prefix[i] = prefix[i - 1] * nums[i - 1]
  for i in range(n - 2, -1, -1):
    postfix[i] = postfix[i + 1] * nums[i + 1]
  
  res = [prefix[i] * postfix[i] for i in range(n)]

  return res

#neetcode solution that is more space efficient by using a single array and doing two passes. first populates it with prefixes and second multiplies them with postfixes
def productExceptSelf(nums):
  n = len(nums)
  res = []
  prefix, postfix = 1,1

  for i in range(n):
    if i == 0:
      res.append(1)
    else:
      prefix = nums[i-1] * prefix
      res.append(prefix)
  
  for i in range(n - 1, -1, -1):
    if i == n - 1:
      res[i] = res[i] * 1
    else:
      postfix = nums[i + 1] * postfix
      res[i] = res[i] * postfix
  
  return res


nums = [1,2,3,4]
print(productExceptSelf(nums))