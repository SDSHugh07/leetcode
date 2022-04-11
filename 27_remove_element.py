class Solution:
    def removeElement(self, nums, val) -> int:

        k=0

        for i in range (len(nums)):
            if nums[i] == val:
                k = i
                break

        for j in range (k,len(nums)):
            if nums[j] == val:
                j+=1
            else:
                nums[k] = nums[j]
                j+=1
                k+=1

        return k

if __name__ == "__main__":
    print("27_remove_element")

    sol = Solution()

    inputs = [[[],3],[[3],3],[[2,3,2,3,3,2,2,3],3], [[3,2,2,3],3], [[3,2,2,3,4],3], [[0,1,2,2,3,0,4,2],2], [[3,3,3,3,3],3]]

    for input in inputs:
        output = sol.removeElement(input[0], input[1])

        print(output)

