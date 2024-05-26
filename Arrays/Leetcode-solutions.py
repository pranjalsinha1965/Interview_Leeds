class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        return (merged[mid] + merged[mid - 1]) / 2.0 if n % 2 == 0 else merged[mid]
    
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=''
        for i in range(len(s)):
            ans=max(ans, expand(s, i, i), expand(s, i ,i+1), key=len)
        return ans
    
def expand(s, i, j):
    while i>=0 and j<len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)

        