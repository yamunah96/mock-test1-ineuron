def firstUniqChar(s):
    freq = {}  
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


s1 = "leetcode"
print(firstUniqChar(s1))
# Output: 0

s2 = "loveleetcode"
print(firstUniqChar(s2))
# Output: 2

s3 = "aabb"
print(firstUniqChar(s3))
# Output: -1
