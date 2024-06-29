class Solution:
    def longest_palindrome(self, s: str) -> int:
        r = 0
        i = 0
        charDictionary = {}
        
        for c in s:
            charDictionary[c] = charDictionary.get(c, 0) + 1
            
        for count in charDictionary.values():
            if count % 2 != 0:
                r += count - 1
                i = 1
            else:
                r += count
                
        return r + i
    
####
solution = Solution()
s = "abccccdd"
print(f"The length of the longest palindrome that can be formed is: {solution.longest_palindrome(s)}")