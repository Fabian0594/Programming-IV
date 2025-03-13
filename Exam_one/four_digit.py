def main():
    
    number = int(input("Enter a four-digit number: "))
    if number < 1000 or number > 9999:
        print("The number is not four digits")
    
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10
    
    if digits[len(digits) - 1] % digits[0] == 0:
        print("The last digit is multiple of the first digit")
        print(f"The sum of the digit 2 and 3 is {digits[1] + digits[2]}")
    else:
        print("The last digit is not multiple of the first digit")
        print(f"The sum of the digit 2 and 3 is {digits[1] + digits[2]}")
    
    
        
if __name__ == "__main__":
    main()
    