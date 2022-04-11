class Solution:
    """
    my original, but it may have been cheating a little to use the pop() function
    """

    # def removeDuplicates(self, nums) -> int:
    #
    #     i = 0
    #
    #     while i < len(nums)-1:
    #         while nums[i] == nums[i+1]:
    #             nums.pop(i+1)
    #             if (i+1) >= len(nums):
    #                 break
    #         i+=1
    #
    #     return len(nums)

    # [0,0,1,1,1,2,2,3,3,4]

    """
    2nd attempt after reviewing the submissions discussions
    """
    def removeDuplicates(self, nums) -> int:

        if len(nums)==1:
            return 1

        k=0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                k=i
                break

        for j in range(k, len(nums)):
            if nums[j] != nums[j-1]:
                nums[k] = nums[j]
                k+=1

        return k

if __name__ == "__main__":
    print("26_remove_duplicates_from_sorted_array")

    sol = Solution()

    inputs = [[1,1,2],[0,0,1,1,1,2,2,3,3,4],[0,1,1,1,1,2,2,3,3,4],[1,1]]

    for input in inputs:
        output = sol.removeDuplicates(input)

        print(output)

