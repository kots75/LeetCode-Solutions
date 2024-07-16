#own solution that uses Counter collection and sorts the dictionary based on the values in descending order
# Time complexity: O(nlogn)
from collections import Counter

def topKFrequent(nums, k):
  counts = Counter(nums)
  res = []
  sortCounts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
  
  for i in range(k):
    res.append(sortCounts[i][0])

  return res

#optimized solution that uses bucket sort. Has a frequency list that stores the numbers based on their frequency
#time complexity: O(n)
def topKFrequent(nums, k):
  counts = {}
  freq = [[] for i in range(len(nums) + 1)]

  for n in nums:
    counts[n] = counts.get(n,0) + 1
  for n, c in counts.items():
    freq[c].append(n)
  
  res = []
  for i in range(len(freq)- 1,0,-1):
    for n in freq[i]:
      res.append(n)
      if len(res) == k:
        return res
  
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))