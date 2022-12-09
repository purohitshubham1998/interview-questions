def numberToWords(num: int) -> str:
    numbers = {
        1000000000: "Billion",
        1000000: "Million",
        1000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
        0: "Zero"
    }
    string = []

    def func(num: int, string):
        if num == 0:
            string.append(numbers[num])
        else:
            for denom in numbers.keys():
                if num == 0:
                    break
                if num >= denom:
                    result = num // denom
                    if result not in numbers:
                        func(result, string)
                    else:
                        if num > 100:
                            string.append(numbers[result])
                    string.append(numbers[denom])
                    num %= denom

    func(num, string)
    return " ".join(string)

result = numberToWords(9100)
print(result)
