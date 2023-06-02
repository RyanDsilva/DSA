class Solution:
    # Recieved 18/20, TLE because of lack of optimization of Sliding Window
    def minSubArrayLenNaive(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        min_subarray_length = 100000
        i = j = 0
        while j < n:
            current_sum = sum(nums[i : j + 1])
            current_length = j - i + 1
            if current_sum >= target and current_length < min_subarray_length:
                min_subarray_length = current_length
            if current_sum >= target:
                if i == j:
                    j = min(j + 1, n)
                else:
                    i = min(i + 1, j)
            else:
                j = min(j + 1, n)
        return min_subarray_length

    # Here, complexity is amortized by ensuring that j goes through the array just once, which makes the average case complexity much better
    # Time Complexity: O(2n)
    # Space Complexity: O(1)
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        min_subarray_length = 100000
        i = 0
        current_sum = 0
        for j in range(0, n):
            current_sum += nums[j]
            while current_sum >= target:
                min_subarray_length = min(min_subarray_length, j - i + 1)
                current_sum -= nums[i]
                i += 1
        return min_subarray_length


s = Solution()
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
