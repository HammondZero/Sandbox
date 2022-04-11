minimum_characters = 2
maximum_characters = 6
special_required = False
special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main(): # main function, main menu
    global key # password
    print("Your password must be between", minimum_characters, "and", maximum_characters, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    print("Please enter a valid password: ")

    if special_required:
        print("\tand 1 or more special characters: ", special_required)
    key = input("> ")
    while not validate_password(key):
        print("Invalid password!")
        key = input("> ")
    print("Your " + str(
        len(key)) + " character password is valid: " + key)

def validate_password(key):
    if len(key) < minimum_characters or len(key) > maximum_characters:
        return False

# set as all character limitations to base set value 0

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special_character = 0
    for char in key:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in special_characters:
            count_special_character += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if special_required: # if more than 0 special characters are detected, reject password
        if count_special_character == 0:
            return False

    return True


main()