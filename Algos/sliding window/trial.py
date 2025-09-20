def lengthOfLongestSubstring(s):
    left=0
    seen=set()
    m=0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[i])
        m=max(m,i-left+1)
    return m

print(lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
print(lengthOfLongestSubstring("")) 