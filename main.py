import sys
from pathlib import Path
import os
import random
import pyfiglet

logo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⣄⠀⠀⠀⠀⠀⠀⣠⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣠⣴⣶⣶⣦⣄⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣉⣉⣉⣉⣉⣉⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
⠀⠀⢸⣿⠟⠛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⠛⠛⠛⠛⢿⡿⠛⠿⣿⡇⠀⠀
⠀⠀⢸⡏⢠⣾⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⣽⡇⠀⠀
⠀⠀⢸⡇⢸⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠿⣿⡇⠀⠀
⠀⠀⢸⡇⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠶⣾⡇⠀⠀
⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠶⢾⡇⠀⠀
⠀⠀⢸⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣷⣶⣶⣿⡇⠀⠀
⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀
"""
greeting_message = pyfiglet.figlet_format("RANDOM WATCH")
show_list = []

def manual_input():
    global show_list
    print("Please enter the shows individually and quit by entering [!STOP]")
    while True:
        show = input("> ")
        show_list.append(show)
        if show == "!STOP":
            return

def file_input():
    global show_list
    while True:
        print("Please enter the file path")
        file_path = input("> ")
        if file_path.startswith("~"):
            file_path = Path(file_path).expanduser()
        else:
            file_path = Path(file_path)

        if file_path.exists():
            break
        else:
            print("File not found...")

    try:
        with open(file_path, "r") as file:
            show_list = file.readlines()
    except:
        print("Failed to open the file...")
        raise

def random_choice():
    global show_list
    random_index = random.randint(0, len(show_list) - 1)
    return show_list[random_index]

try:
    print(logo)
    print(greeting_message)
    while True:
        print("Do you want to manually input all of the shows or enter a complete txt file instead? (m/f)")
        user_choice = input("> ")
        if user_choice == "m":
            manual_input()
            print(f"-----------\nYour next watch is: {random_choice()}")
            break
        elif user_choice == "f":
            file_input()
            print(f"-----------\nYour next watch is: {random_choice()}")
            break
        else: print("Please enter a valid choice")

except KeyboardInterrupt:
    print("\nStopping script...")
    sys.exit(0)