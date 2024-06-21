#My solution that works perfectly but is just less concise
# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#       return False
    
#     #key letter : value frequency
#     sDict = {}
#     tDict = {}

#     for char in s:
#       if char in sDict:
#         sDict[char] += 1
#       else:
#         sDict[char] = 1

#     for char in t:
#       if char in tDict:
#         tDict[char] += 1
#       else:
#         tDict[char] = 1

#     if sDict.keys() != tDict.keys():
#       return False

#     for l in sDict:
#       if sDict[l] == tDict[l]:
#         continue
#       else:
#         return False
#     return True

#Optimized solution from NeetCode that is more concise but uses the same logic
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for l in countS:
        if countS[l] != countT.get(l, 0):
            return False
        
    return True
    
        

s = "rat"
t = "car"
print(isAnagram(s,t))