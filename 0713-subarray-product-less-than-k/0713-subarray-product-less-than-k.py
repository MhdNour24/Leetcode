class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:


        counter = 0
        left = 0  # Sliding window left pointer
        product = 1  # Current product within the window

        for right in range(len(nums)):
            product *= nums[right]

            # Shrink the window while the product is greater than or equal to k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # Count all subarrays ending at 'right' (including single elements)
            counter += right - left + 1

        return counter
