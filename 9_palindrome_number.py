
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """

        str_val = str(x)
        str_rev = txt = str_val[::-1]

        if str_rev == str_val:
            return True
        else:
            return False

if __name__ == "__main__":
    print("9_palindrome_number")

    inputs = [121, -121, 10, 99, 103]

    for input in inputs:
        output = isPalindrome(input)

        print(output)

