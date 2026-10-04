Sarabianame = input("Name: ")

Canonocalculator = input('''\nChoose from below to calculate:\n|Power|\n|Voltage|\n|Current|\n\n''').strip().capitalize()

if Canonocalculator == "Power":
    Canonocurrent = float(input("Current: "))
    Canonovoltage = float(input("Voltage: "))
    Canonopower = Canonocurrent * Canonovoltage
    print (f"Power is {Canonopower:,.2f} Watt/s.")
elif Canonocalculator == "Current":
    Canonopower = float(input("Power: "))
    Canonovoltage = float(input("Voltage: "))
    Canonocurrent = Canonopower / Canonovoltage
    print(f"Current is {Canonocurrent:,.2f} Ampere/s.")
elif Canonocalculator == "Voltage":
    Canonopower = float(input("Power: "))
    Canonocurrent= float(input("Current: "))
    Canonovoltage = Canonopower / Canonocurrent
    print(f"Voltage is {Canonovoltage:,.2f} Volt/s.")
else:
    print("Invalid input")