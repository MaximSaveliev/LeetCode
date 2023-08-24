class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for digit in digits:
            number += str(digit)

        number = str(int(number) + 1)
        result = []
        for digit in number:
            result.append(int(digit))
        return result