class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    # Create a set based off of the nums list argument because sets can't contain duplicates
    num_set = set(nums)
    
    # Check if the length of the set is different than the length of the list argument
    if len(num_set) != len(nums): 
      # If the lengths aren't the same, a duplicate was present
      return True
    else: 
      return False
