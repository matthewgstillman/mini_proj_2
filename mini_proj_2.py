#Mini Project #2
#Your program should convert any decimal integer into a 16-bit binary number and a 4-bit hexadecimal
#numbers. To make it easier, lets assume it is only an integer. As a challenge, if you want, you can write
#one that takes in a floating point number as well.
#Any numbering system can be summarized by the following relationship:


binary_hex_decimal_dict = {
    '0000': {
        'binary': '0000',
        'hex': 0,
        'decimal': 0,
    },
    '0001': {
        'binary': '0001',
        'hex': 1,
        'decimal': 1,
    },
    '0010': {
        'binary': '0010',
        'hex': 2,
        'decimal': 2,
    },
    '0011': {
        'binary': '0011',
        'hex': 3,
        'decimal': 3,
    },
    '0100': {
        'binary': '0100',
        'hex': 4,
        'decimal': 4,
    },
    '0101': {
        'binary': '0101',
        'hex': 5,
        'decimal': 5,
    },
    '0110': {
        'binary': '0110',
        'hex': 6,
        'decimal': 6,
    },
    '0111': {
        'binary': '0111',
        'hex': 7,
        'decimal': 7,
    },
    '1000': {
        'binary': '1000',
        'hex': 8,
        'decimal': 8,
    },
    '1001': {
        'binary': '1001',
        'hex': 9,
        'decimal': 9,
    },
    '1010': {
        'binary': '1010',
        'hex': 'A',
        'decimal': 10,
    },
    '1011': {
        'binary': '1011',
        'hex': 'B',
        'decimal': 11,
    },
    '1100': {
        'binary': '1100',
        'hex': 'C',
        'decimal': 12,
    },
    '1101': {
        'binary': '1101',
        'hex': 'D',
        'decimal': 13,
    },
    '1110': {
        'binary': '1110',
        'hex': 'E',
        'decimal': 14,
    },
    '1111': {
        'binary': '1111',
        'hex': 'F',
        'decimal': 15,
    },
}

binary = ""
number = 0
digit_count = 0

binary = ""
number = 0
digit_count = 0

user_number = int(input("Enter a number: "))
division = user_number // 2
remainder = user_number % 2

if division != 0:
    binary += str(remainder)
    user_number = division
    division = user_number // 2
    remainder = user_number % 2
    binary += str(remainder)
    user_number = division
    division = user_number // 2
    remainder = user_number % 2
    binary += str(remainder)
    user_number = division
    division = user_number // 2

if division == 0:
    division = user_number // 2
    remainder = user_number % 2
    binary += str(remainder)

final_binary_number = binary[3::-1]
print("Final Binary Number: {}".format(final_binary_number))
print(binary_hex_decimal_dict[final_binary_number])