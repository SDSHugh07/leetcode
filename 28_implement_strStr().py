class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j=i
                for k in range(len(needle)):
                        if j<len(haystack) and haystack[j] == needle[k]:
                            j+=1
                        else:
                            break

                if j-i == len(needle):
                    return i

        return -1



if __name__ == "__main__":
    print("28_implement_strStr()")

    sol = Solution()

    inputs = [["","hell"],["helello","ll"],["hello", "ll"],["aaaaa","bba"], ["mississippi","issipi"]]

    for input in inputs:
        output = sol.strStr(input[0], input[1])

        print(output)

