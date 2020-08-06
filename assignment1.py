""""
Replace the contents of this module docstring with your own details
Name: Jerome Ribaldone
Date started:28/08/2020
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-1-Jerome-Ribaldone
"""
from operator import itemgetter

# Constant for menu and file name
MENU = """Menu:
L - List places
A - Add new place
M - Mark a place as visited
Q - Quit"""
FILE_NAME = "places.csv"


def load_places():
    "Retrieves all data from FILE_NAME"
    # tries to open file from constant
    try:
        # reads file
        places_file = open(FILE_NAME, "r")
        # creates list and variables
        places = []
        places_found = 0
        places_unvisited = 0
        # formats csv file in to nested list
        for i in places_file:
            places.append(i.split(","))
            try:
                places[places_found][2] = int(places[places_found][2])
            # if the file is formatted wrong the program doesnt work
            except ValueError:
                print(f"The formatting of {FILE_NAME} is Wrong.")
            # count how many unvisited places there are
            if places[places_found][3] == "n\n":
                places_unvisited += 1
            # counts total places
            places_found += 1
        places_file.close()
        return places, places_found, places_unvisited
    # if file name is wrong or cannot be found this will be outputted
    except FileNotFoundError:
        print(f"Sorry, {FILE_NAME} cannot be found")


def add_places(places, places_found):
    """
    Get all inputs and error check
    then add to places
    """
    # creates list for new place
    new_place = []
    # gets name, country and priority
    name = validate_input_str("Name: ").capitalize()
    country = validate_input_str("Country: ").capitalize()
    priority = int(validate_input_int("Priority: "))
    # adds all prior inputs to new place list
    new_place.append(name)
    new_place.append(country)
    new_place.append(priority)
    new_place.append("n\n")
    # adds new place to places
    places.append(new_place)
    # then adds 1 to total of places
    places_found += 1
    return places_found


def display_places(places, places_found, places_unvisited):
    """
    display and sort all places
    """
    # sorts items by not visited then, priority
    places.sort(key=itemgetter(3, 2))
    # displays formatted list and checks if not visited
    for i in range(len(places)):
        if places[i][3] == "n\n":
            print(f"*{i + 1}. {places[i][0]:<10} in {places[i][1]:<12} priority {places[i][2]:>4}")
        else:
            print(f" {i + 1}. {places[i][0]:<10} in {places[i][1]:<12} priority {places[i][2]:>4}")
    # if places_visited is greater than 0 display how many left else display none left
    if places_unvisited > 0:
        print(f"{places_found} places. You still want to visit {places_unvisited} places")
    else:
        print(f"{places_found} places. No places left to visit, Why not add a new place?")


def validate_input_int(variable):
    """
    Validates the input of an integer. If not valid function will repeat until is valid
    """
    validate_input = False
    while not validate_input:
        try:
            # checks integer input and displays variable
            int_input = int(input(f"{variable}"))
            # if input is blank prints message and repeats
            if int_input == "":
                print("Input can not be blank")
            elif int_input < 0:
                print("Number Must be > 0")
            else:
                validate_input = True
                return int_input
        except ValueError:
            print("Invalid input; enter valid input")


def validate_input_str(variable):
    """
    validates the input in a string, if not valid, repeats until user does input correctly
    """
    validate_input = False
    # checks string input and displays variable
    while not validate_input:
        str_input = str(input(f"{variable}"))
        # if input is blank prints message and repeats
        if str_input == "":
            print("Input can not be blank")
        else:
            validate_input = True
            return str_input


def mark_location_as_visited(places, places_unvisited, places_found):
    """
    Marks location as visited by changing places[x][3] to v\n
    """
    # Check if there are any places unvisited
    if places_unvisited > 0:
        # Displays places
        display_places(places, places_found, places_unvisited)
        print("Enter the number of the place to mark as visited")
        # Gets value corresponding with place
        place_to_mark = validate_input_int(">>> ") - 1
        #     if value = a place already visited, displays place already visited
        while place_to_mark > len(places):
            print("Invalid place number")
            place_to_mark = validate_input_int(">>> ") - 1
            print("Invalid place number")
        if places[place_to_mark][3] == "v\n":
            print("That Place is already visited")
        # marks place unvisited to visited
        else:
            print(f"{places[place_to_mark][0]} in {places[place_to_mark][1]} visited!")
            places_unvisited -= 1
            places[place_to_mark][3] = "v\n"

    else:
        print("No unvisited places")
    return places_unvisited


def save_places(places):
    """"
    Saves all places to FILE_NAME
    """
    # opens file to write
    places_file = open(FILE_NAME, "w")
    # saves all files to FILE_NAME
    for x in range(len(places)):
        places[x][0] += ","
        places[x][1] += ","
        places[x][2] = str(places[x][2])
        places[x][3] += ","
        places_file.writelines(places[x][0] + places[x][1] + places[x][2] + places[x][3])


def quit_program(places_found):
    """"
    Displays quit message
    """
    print(f"{places_found} places saved to {FILE_NAME}")
    print("Have a nice day :)")


def main():
    """"
    Menu for program
    """
    print("Travel Tracker 1.0 - by Jerome Ribaldone")
    # places variables into main
    places, places_found, places_unvisited = load_places()
    print(f"{places_found} places loaded from {FILE_NAME}")
    # menu loop
    menu_loop = 0
    while menu_loop == 0:
        menu_loop += 1
        print(MENU)
        user_menu_input = (input(">>> ")).upper()
        if user_menu_input == "L":
            display_places(places, places_found, places_unvisited)
        elif user_menu_input == "A":
            add_places(places, places_found)
        elif user_menu_input == "M":
            mark_location_as_visited(places, places_unvisited, places_found)
        elif user_menu_input == "Q":
            save_places(places)
            quit_program(places_found)
            menu_loop = menu_loop - 1
        # error check for invalid input
        else:
            print("Invalid menu choice")
        menu_loop = menu_loop - 1


if __name__ == '__main__':
    main()
