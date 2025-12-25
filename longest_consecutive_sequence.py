# Problem: Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.
        
        APPROACH: Hash Set + Intelligent Sequence Building
        -------------------------------------------------
        1. Convert list to a set for O(1) lookups.
        2. Iterate through the set.
        3. CRITICAL OPTIMIZATION: Only attempt to count a sequence if 'num' is 
           the *start* of a sequence (i.e., num-1 is NOT in the set).
           This ensures we don't redundantly count from the middle of a chain.
           
        COMPLEXITY ANALYSIS:
        --------------------
        - Time: O(n)
          Although there is a nested while loop, each number is visited at most 
          twice: once by the outer loop, and once by the inner loop.
        - Space: O(n) 
          Used to store the set of numbers.
        """
        if not nums:
            return 0
        
        nums_set = set(nums)
        longest_streak = 0
        
        for num in nums_set:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                longest_streak = max(longest_streak, length)
                
        return longest_streak

# ---------------------------------------------------
# Execution & Testing
# ---------------------------------------------------
if __name__ == "__main__":
    solver = Solution()

    # Case 1: Standard Example
    # Sequence: [1, 2, 3, 4] -> Length 4
    nums1 = [100, 4, 200, 1, 3, 2]
    assert solver.longestConsecutive(nums1) == 4, f"Failed Case 1: Got {solver.longestConsecutive(nums1)}"

    # Case 2: Duplicates (Set should handle this)
    # Sequence: [0, 1, 2, 3, 4, 5, 6] -> Length 7
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert solver.longestConsecutive(nums2) == 9, f"Failed Case 2: Got {solver.longestConsecutive(nums2)}"

    # Case 3: Empty List
    nums3 = []
    assert solver.longestConsecutive(nums3) == 0, "Failed Case 3 (Empty)"

    # Case 4: Negative Numbers
    # Sequence: [-1, 0, 1] -> Length 3
    nums4 = [-1, -2, -3, 0, 1] 
    # Actually wait, sequence is [-3, -2, -1, 0, 1] -> Length 5
    assert solver.longestConsecutive(nums4) == 5, f"Failed Case 4: Got {solver.longestConsecutive(nums4)}"

    # Case 5: Single Element
    nums5 = [10]
    assert solver.longestConsecutive(nums5) == 1, "Failed Case 5 (Single)"
    
    # Case 6: Multiple separate sequences
    # Sequences: [1,2,3] (len 3) and [10,11,12,13,14] (len 5)
    nums6 = [1, 2, 3, 10, 11, 12, 13, 14]
    assert solver.longestConsecutive(nums6) == 5, f"Failed Case 6: Got {solver.longestConsecutive(nums6)}"

    print("All test cases passed!")