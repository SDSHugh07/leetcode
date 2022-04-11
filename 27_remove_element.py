class Solution:
    def removeElement(self, nums, val) -> int:

        k=0

        for j in range (len(nums)):
            if nums[j] != val:
                nums[k] = nums[j]
                k+=1

        return k

if __name__ == "__main__":
    print("27_remove_element")

    sol = Solution()

    inputs = [[[],3],[[3],3],[[2,3,2,3,3,2,2,3],3], [[3,2,2,3],3], [[3,2,2,3,4],3], [[0,1,2,2,3,0,4,2],2], [[3,3,3,3,3],3]]

    for input in inputs:
        output = sol.removeElement(input[0], input[1])

        print(output)

