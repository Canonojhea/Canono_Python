Canononame = input("Enter Employee Name: ")
Canonocategory = input("Enter Employee Category:\n|A| for Regular Employee\n|B| for Part-Time Employee\n|C| for Contract Employee\n|D| for Manager\n")

match Canonocategory.strip().capitalize():
    case "A":
        CanonohoursWorked = int(input("Enter of hours worked: "))
        CanonohourlyRate = float(input("Enter hourly rate: "))
        Canonobonus = 2000
        Canonodesc = "Regular Employee"
        if CanonohoursWorked > 40:
            OTCanonorate = CanonohourlyRate * 1.5
            OTCanonoPay = (CanonohoursWorked - 40) * OTCanonorate
        else:
            print("Invalid Input")

    case "B":
        CanonohoursWorked = int(input("Enter of hours worked: "))
        CanonohourlyRate = float(input("Enter hourly rate: "))
        Canonobonus = 500
        Canonodesc = "Part-Time Employee"

    case "C":
        CanonohoursWorked = int(input("Enter of hours worked: "))
        CanonohourlyRate = float(input("Enter hourly rate: "))
        OTCanonorate = 1.25
        Canonobonus = 1000
        Canonodesc = "Contract Employee"
        if CanonohoursWorked > 40:
            OTCanonorate = CanonohourlyRate * 1.25
            OTCanonoPay = (CanonohoursWorked - 40) * OTCanonorate

    case "D":
        CanonohoursWorked = int(input("Enter of hours worked: "))
        CanonohourlyRate = float(input("Enter hourly rate: "))
        Canonobonus = 5000
        Canonodesc = "Manager"

    case _:
        print("Invalid Input")

if (CanonohoursWorked >40):
    CanonoregularPay = 40 * CanonohourlyRate
else:
    CanonoregularPay = CanonohoursWorked * CanonohourlyRate

CanonogrossSalary = CanonoregularPay + OTCanonoPay + Canonobonus

print(f"\nEmployee name: {Canononame.title()}\nEmployee Category: {Canonodesc}\nNumber of hours worked: {CanonohoursWorked}\nHourly Rate: {CanonohourlyRate}\n",
f"\nRegular Pay: {CanonoregularPay}\nOvertime Pay: {OTCanonoPay}\nBonus: {Canonobonus}\nGross Salary: {CanonogrossSalary}")