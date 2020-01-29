def romanConverter(num):

    # Checking invalid input

    if num == 0:
        return "Error, no zero conversion"
    if num < 0:
        return "Error, negative number"

    remainder = num
    roman = ""

    while remainder > 0:
        if (remainder >= 1000):
            remainder -= 1000
            roman += "M"
        elif (remainder >= 900):
            remainder -= 900
            roman += "CM"
        elif (remainder >= 500):
            remainder -= 500
            roman += "D"
        elif (remainder >= 400):
            remainder -= 400
            roman += "CD"
        elif (remainder >= 100):
            remainder -= 100
            roman += "C"
        elif (remainder >= 90):
            remainder -= 90
            roman += "XC"
        elif (remainder >= 50):
            remainder -= 50
            roman += "L"
        elif (remainder >= 40):
            remainder -= 40
            roman += "XL"
        elif (remainder >= 10):
            remainder -= 10
            roman += "X"
        elif (remainder >= 9):
            remainder -= 9
            roman += "IX"
        elif (remainder >= 5):
            remainder -= 5
            roman += "V"
        elif (remainder >= 4):
            remainder -= 4
            roman += "IV"
        elif (remainder >= 1):
            remainder -= 1
            roman += "I"

    return roman
