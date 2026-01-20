import sys
from pathlib import Path
import random
import pyfiglet
import requests

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
        if show == "!STOP":
            return
        else:
            show_list.append(show)

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
    return {'title': show_list[random_index], 'index': random_index+1}

def search_anime(query):
    # Jikan API Search Endpoint
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=1"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        data = response.json()

        if data['data']:
            anime = data['data'][0]

            result = {
                "title": anime['title'],
                "url": anime['url'],
                "score": anime['score'],
            }
            return result
        else:
            return "No results found on MAL."

    except Exception as e:
        return f"Error while looking up the anime title: {e}"

try:
    print(logo)
    print(greeting_message)
    while True:
        print("Do you want to manually input all of the shows or enter a complete txt file instead? (m/f)")
        user_choice = input("> ")
        if user_choice == "m":
            manual_input()
            choice = random_choice()
            print(f"-----------\nYour next watch is option number {choice['index']}")
            print("Title: ", choice['title'])
            anime_info = search_anime(choice['title'])
            if isinstance(anime_info, dict):
                print(f"Score: {anime_info['score']}")
                print(f"MAL Link: {anime_info['url']}")
            else:
                print(anime_info)
            break
        elif user_choice == "f":
            file_input()
            choice = random_choice()
            print(f"-----------\nYour next watch is option number {choice['index']}")
            print("Title: ", choice['title'])
            anime_info = search_anime(choice['title'])
            if isinstance(anime_info, dict):
                print(f"Score: {anime_info['score']}")
                print(f"MAL Link: {anime_info['url']}")
            else:
                print(anime_info)
            break
        else: print("Please enter a valid choice")

except KeyboardInterrupt:
    print("\nStopping script...")
    sys.exit(0)