while True:
    word = input("Enter the word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for letter in word:
        if character.lower() == letter.lower():
            found = True
            break

    if found:
        print("Character Found!")
    else:
        print("Character Not Found.")

    again = input("try again? (y/n): ")

    if again.upper() != "Y":
        break