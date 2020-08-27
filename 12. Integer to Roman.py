class Solution:
    def intToRoman(self, num: int) -> str:
        result = "" + num // 1000 * 'M'
        num = num % 1000

        if num >= 900:
            result += "CM"
            num -= 900
        elif num >= 500:
            result = result + num // 500 * "D"
            num = num % 500
            result = result + num // 100 * "C"
            num = num % 100
        elif num >= 400:
            result += "CD"
            num -= 400
        else:
            result = result + num // 100 * "C"
            num = num % 100

        if num >= 90:
            result += "XC"
            num -= 90
        elif num >= 50:
            result = result + num // 50 * "L"
            num = num % 50
            result = result + num // 10 * "X"
            num = num % 10
        elif num >= 40:
            result += "XL"
            num -= 40
        else:
            result = result + num // 10 * "X"
            num = num % 10

        if num >= 9:
            result += "IX"
            num -= 90
        elif num >= 5:
            result = result + num // 5 * "V"
            num = num % 5
            result = result + num // 1 * "I"
            num = num % 1
        elif num >= 4:
            result += "IV"
            num -= 4
        else:
            result = result + num // 1 * "I"
        return result

