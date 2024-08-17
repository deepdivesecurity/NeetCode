from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Get the character counts as a hashtable
        s_count = Counter(s)
        t_count = Counter(t)

        # Check if the hashtables are equal
        if s_count == t_count: 
            return True
        else: 
            return False
