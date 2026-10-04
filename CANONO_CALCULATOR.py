Canononum1 = int(input("Enter a number: "))
Canononum2 = int(input("Enter another number: "))
Canonooperator = input("Enter operator: ")

if Canonooperator == "+":
    sum = Canononum1 + Canononum2
    print(sum)
elif Canonooperator == "-":
    difference = Canononum1 - Canononum2
    print(difference)
elif Canonooperator == "*":
    product = Canononum1 * Canononum2
    print(product)
elif Canonooperator == "/":
    quotient = Canononum1 / Canononum2
    print(quotient)
else:
    print("Invalid operator/input")