class Solution:
    def searchInsert(self, nums, target: int) -> int:

        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)

        low = 0
        mid = int(len(nums) / 2)
        hi = len(nums) - 1

        while low <= hi:
            if target < nums[mid]:
                hi = mid-1
            elif target == nums[mid]:
                return mid
            else:
                low = mid+1
            mid = low + int((hi - low) / 2)

        return low

if __name__ == "__main__":
    print("35_search_insert_position")

    sol = Solution()

    inputs = [[[1,3,5,6],5], [[1,3,5,6],2], [[1,3,5,6],7], [[1,3],2]]

    for input in inputs:
        output = sol.searchInsert(input[0], input[1])

        print(output)

