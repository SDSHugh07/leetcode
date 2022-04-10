
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    dict = {}
    idx = 0

    for i in range(len(nums)):
        if nums[i] in dict:
            num = nums[i]
            if num*2 == target:
                return [dict[num], idx]
        dict[nums[i]] = i
        idx += 1

    for val in dict:
        idx = dict[val]

        seeking = target - val

        if seeking in dict and (dict[seeking] != idx):
            idx_seeking = dict[seeking]
            return [idx, idx_seeking]
    """
    #approach #2 - Two-pass Hash Table
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    """
    """
    Approach 3: One-pass Hash Table
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    """

if __name__ == "__main__":
    print("1_two_sum")

    inputs = [[[2,7,11,15],9], [[3,2,4],6], [[3,3],6], [[2,7,11,15],18]]

    for input in inputs:
        nums = input[0]
        target = input[1]

        output = twoSum(nums,target)

        print(output)

