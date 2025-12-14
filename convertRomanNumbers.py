def convertRomanToInt(s):
    result = 0
    dictRoman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if "IV" in s or "IX" in s:
        f = s.count("IV") + s.count("IX")
        result -= 2 * f
    if "XL" in s or "XC" in s:
        r = s.count("XL") + s.count("XC")
        result -= 20 * r
    if "CD" in s or "CM" in s:
        t = s.count("CD") + s.count("CM")
        result -= 200 * t

    for i in s:
        result += dictRoman.get(i)

    print(result)
    return result
