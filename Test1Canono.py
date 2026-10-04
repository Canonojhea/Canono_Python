from typing import Sized

Canononame = (input("Name: "))
CanonocoffeeSize = (input("\nChoose Coffee Size:\nSmall\nMedium\nLarge\n\n").strip().capitalize())
CanonoextraShot = (input("\nExtra Shot?\nYes\nNo\n\n").strip().capitalize())

if CanonocoffeeSize == "Small".strip().capitalize():
    smallPrice: int = 80
    if CanonoextraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
elif CanonocoffeeSize == "Medium".strip().capitalize():
    mediumPrice: int = 100
    if CanonoextraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
elif CanonocoffeeSize == "Large".strip().capitalize():
    largePrice: int = 120
    if CanonoextraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
else:
    print("Please choose a coffee size")



print ("===== COFFEE RECEIPTS =====")
print ("Customer: ", Canononame)
print ("Coffee Size: ", CanonocoffeeSize)
print ("Extra Shot: ", CanonoextraShot)
print ("Total: ",)