class Solution:
    def longestCommonPrefix(self, strs) -> str:

        prefix = ""

        for i in range(len(strs[0])):
            prefix += strs[0][i]
            for str in strs:
                if not str.startswith(prefix):
                    return prefix[:i]

        return prefix


if __name__ == "__main__":
    print("13_longest_common_prefix")

    sol = Solution()

    inputs = [["flower","flow","flight"],["dog","racecar","car"], ["ca", "cad", "cade"]]

    for input in inputs:
        output = sol.longestCommonPrefix(input)

        print(output)

