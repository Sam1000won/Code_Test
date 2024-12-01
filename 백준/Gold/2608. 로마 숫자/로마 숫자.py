def roman_to_arabic(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
        
    return total

def arabic_to_roman(num):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    roman = ""
    
    for value, symbol in roman_numerals:
        while num >= value:
            roman += symbol
            num -= value
    
    return roman

roman1 = input().strip()
roman2 = input().strip()

arabic1 = roman_to_arabic(roman1)
arabic2 = roman_to_arabic(roman2)
total_arabic = arabic1 + arabic2
total_roman = arabic_to_roman(total_arabic)

print(total_arabic)
print(total_roman)