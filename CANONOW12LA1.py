CanonoSalary = {"E104": {
                    "Employee Name": "Cheijay Loberiza",
                    "Daily Hours": [8, 9, 8.5, 10, 8]
},
                "E601": {
                    "Employee Name": "Datrell Falcon",
                    "Daily Hours": [9, 10, 8, 8, 9]
    }
}

CanonoEmpInfo = ""
CanonoOT = 0
CanonoWeeklyBasic = 9000
CanonoRateperHour = CanonoWeeklyBasic / 40

for CanonoEmp_ID, CanonoEmpInfo in CanonoSalary.items():
    print(f"ID: {CanonoEmp_ID} | Name: {CanonoEmpInfo['Employee Name']} | Hours: {CanonoEmpInfo['Daily Hours']}")
    print()

CanonoSearch = input("Search for Employee ID: ").upper()
print("Running Employee ID match for: ", CanonoSearch)

Canonofound = False

for CanonoEmp_ID, CanonoEmpInfo in CanonoSalary.items():
    if CanonoSearch == CanonoEmp_ID:
        print(f"Name: {CanonoEmpInfo['Employee Name']}"
              f"\nDuty Hours: {', '.join(map(str, CanonoEmpInfo['Daily Hours']))}")
        Canonofound = True

        CanonoOT = 0
        for hours in CanonoEmpInfo['Daily Hours']:
            if hours > 8:
                CanonoOT += (hours - 8) * (1.5 * CanonoRateperHour)
                print(f"\nExcess Hours: {(hours - 8)}"
                      f"\nRate per Hour: {CanonoRateperHour}")
        GrossPay = (40 * CanonoRateperHour) + CanonoOT
        print(f"\nTotal overtime pay: {CanonoOT:,.2f}"
              f"\nWeekly Basic: {CanonoWeeklyBasic}"
              f"\nGross Pay: {GrossPay:,.2f}")

if not Canonofound:
    print("Invalid Employee ID.")