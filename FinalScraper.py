############ Final oddsportal scraper

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
""" Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games
NB : You need to be in the right repository to import functions..."""

# os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *
from sports import sports

print("Data will be saved in the following directory:", os.getcwd())

# the NBA is not available from oddsportal.com
# this is a list of other leagues I will find the seasons and length of pages available for.
if_poc_passes = """
        5. Japanese J1 ⚽ 🇯🇵
        6. Australian A-League ⚽ 🇦🇺
        7. Brazilian Series A ⚽ 🇧🇷
        8. English Premier ⚽ 🇬🇧
        9. English League Championship ⚽ 🇬🇧
        10. English League One ⚽ 🇬🇧
        11. English League Two ⚽ 🇬🇧
        12. Swedish Allsvenskan ⚽ 🇸🇪
        13. French League One ⚽ 🇫🇷
        14. Italy Series A ⚽ 🇮🇹
        15. Spanish Premier ⚽ 🇪🇸
        16. Mexico MX ⚽ 🇲🇽"""


def menu():
    print_menu = True
    while print_menu:
        print(
            """
        Select a sports league to scrape:
        1. NFL 🏈 🇺🇸
        2. NHL 🏒 🇺🇸
        3. MLB ⚾️ 🇺🇸
        4. MLS ⚽️ 🇺🇸
        0. Exit
        """
        )
        choice = int(input("Enter your choice: "))
        if choice in range(1, 17):
            sub_menu(sports[choice])
        if choice == 0:
            print_menu = False
        else:
            print("Invalid input, please try again.")
            menu()


def sub_menu(sports_choice):
    print_sub_menu = True
    seasons = [
        f"{index + 1}. {season['year']}"
        for index, season in enumerate(sports_choice["seasons"])
    ]

    while print_sub_menu:
        print("Select a season to scrape:")
        print(*seasons, sep="\n")
        print("0. Go Back to Sports Menu")
        choice = int(input("Enter your choice: "))
        if choice in range(1, len(seasons) + 1):
            scrape_oddsportal_historical(
                sport=sports_choice["sport"],
                country=sports_choice["country"],
                league=sports_choice["league"],
                start_season=sports_choice["seasons"][choice - 1]["year"],
                current_season="no",
                max_page=sports_choice["seasons"][choice - 1]["pages"],
            )
        elif choice == 0:
            print_sub_menu = False
            menu()
        else:
            print("Invalid input, please try again.")
            sub_menu(sports_choice)


menu()
