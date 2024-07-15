#less efficient solution that uses sorting on the strings and then groups them based on sorted results

# from collections import defaultdict
# def groupAnagrams(strs):
#   result = defaultdict(list)

#   for i in range(len(strs)):
#     chars = [char for char in strs[i]]
#     chars = "".join(sorted(chars))
#     result[chars].append(strs[i])

#   return list(result.values())



#more efficient O(m * n) solution where we take an array that has frequencies of each character in the string and then convert it to a tuple and then group them based on the tuple

from collections import defaultdict
def groupAnagrams(strs):
  result = defaultdict(list) #mapping charCount to list of anagrams

  for s in strs:
    count = [0] * 26 # a ... z

    for c in s:
      count[ord(c) - ord('a')] += 1
    
    result[tuple(count)].append(s)

  return list(result.values()) 

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))