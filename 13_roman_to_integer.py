class Solution (object):
    values = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100,
                   "CD": 400, "D": 500, "CM": 900, "M": 1000}

    specials = ["IV", "IX", "XL", "XC", "CD", "CM"]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        val = 0

        i = 0

        while i < len(s):
            if s[i:i+2] in self.specials:
                numeral = s[i:i+2]
                i = i+1
            else:
                numeral = s[i]

            i = i + 1

            val += self.values[numeral]

        return val

if __name__ == "__main__":
    print("13_roman_to_integer")

    sol = Solution()


    inputs = ["III", "LVIII", "MCMXCIV"]

    for input in inputs:
        output = sol.romanToInt(input)

        print(output)

