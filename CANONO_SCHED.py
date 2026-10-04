days = (int(input("Choose a day: "
               "\n|1|Monday"
               "\n|2|Monday"
               "\n|3|Tuesday"
               "\n|4|Wednesday"
               "\n|5|Thursday"
               "\n|6|Friday"
               "\n|7|Saturday\n")))
match days:
    case 2:
        time = int(input("Choose a time: 0-23 (Army Hours)"))
        if time == 0 and time >= 6:
            print ("Freetime")
        elif time >= 7 and time <= 9:
            print ("Class: CCINCOML")
        elif time >= 9 and time <= 11:
            print ("Class: GEUTS01X")
        elif time >= 11 and time <= 13:
            print ("Freetime")
        elif time >= 13 and time <= 17:
            print ("Class: CCPRGG1L")
        else:
            print ("Freetime")