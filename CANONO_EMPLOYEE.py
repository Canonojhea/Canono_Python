Canononame = input("Employee Name: ")
jobPosition = input("Input letter for respective job position:\n|A| Janitor\n|B| Clerk\n|C| Cashier\n|D| Manager\n")
hrsWorked = int(input("Actual Hours Worked: "))

absentHrs = 0
absentDeduc = 0
OTHrs = 0
OTPay = 0

match jobPosition.strip().capitalize():
    case "A":
        jobCategory = "Janitor"
        monthlySalary = 18000

    case "B":
        jobCategory = "Clerk"
        monthlySalary = 22000

    case "C":
        jobCategory = "Cashier"
        monthlySalary = 24000

    case "D":
        jobCategory = "Manager"
        monthlySalary = 40000

halfMonthlySalary = monthlySalary / 2
hrlyRate = halfMonthlySalary / 88
if hrsWorked < 88:
    absentHrs = 88 - hrsWorked
    absentDeduc = absentHrs * hrlyRate
elif hrsWorked > 88:
    OTHrs = hrsWorked - 88
    OTRate = hrlyRate * 1.25
    OTPay = OTHrs * OTRate
else:
    pass
netSalary = halfMonthlySalary - absentDeduc + OTPay

print(f"\n\n{'PAYROLL':=^40}")
print(f"\nEmployee Name: {name.title()}"
      f"\nJob Position: {jobCategory}"
      f"\nActual Hours Worked: {hrsWorked} Hours"
      f"\nMonthly Salary: PHP {monthlySalary:,}"
      f"\nHalf-Month Salary: PHP {halfMonthlySalary:,}"
      f"\nHourly Rate: {hrlyRate:,.2f}x")
print(f"\nAbsent Hours: {absentHrs} Hours"
      f"\nExpected Absent Deduction: PHP {absentDeduc:,.2f}"
      f"\nOvertime Hours: {OTHrs:,.2f} Hours"
      f"\nExpected Overtime Pay: PHP {OTPay:,.2f}")
print(f"\nExpected Net Salary: PHP {netSalary:,.2f}")