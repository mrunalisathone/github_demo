# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def find_all_pallindrome_numbers(number):
    for number in range(1000, 10000):
        rev = int(str(number)[::-1])
        if number * 4 == rev:
            return number


x = find_all_pallindrome_numbers()
print(x)