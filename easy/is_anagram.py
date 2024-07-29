from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Get the character counts as a hashtable
        sCount = Counter(s)
        tCount = Counter(t)

        # Check if the hashtables are equal
        if sCount == tCount: 
            return True
        else: 
            return False
