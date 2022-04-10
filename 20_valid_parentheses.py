class Solution:

    lst_close = [")", "}", "]"]
    dct_pairs = {")":"(", "}":"{", "]":"["}


    def isValid(self, s) -> bool:

        stack = []

        for char in s:
            if char in self.lst_close:
                if len(stack) == 0:
                    return False
                if stack[-1] == self.dct_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return (len(stack)==0)

if __name__ == "__main__":
    print("20_valid_parentheses")

    sol = Solution()

    inputs = ["()", "()[]{}", "(]", "{{}[][[[]]]}", "]", "(({}}))", "{", "(({{}))"]

    for input in inputs:
        output = sol.isValid(input)

        print(output)

