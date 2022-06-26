############ Final oddsportal scraper

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
""" Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games
NB : You need to be in the right repository to import functions..."""

# os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *
from sports import sports

# print("Data will be saved in the following directory:", os.getcwd())

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


def wipe_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Menu:
    def __init__(self, print_menu=True):
        self.print_sub_menu = None
        self.print_menu = print_menu
        self.padding = "            "

    def menu(self):
        while self.print_menu:
            # clear the screen
            wipe_screen()
            print(
                """Select a sports league to scrape:
            1. NFL 🏈 🇺🇸
            2. NHL 🏒 🇺🇸
            3. MLB ⚾️ 🇺🇸
            4. MLS ⚽️ 🇺🇸
            0. Exit
            """
            )
            try:
                choice = int(input("Enter your choice: "))
                if choice in range(1, 17):
                    self.sub_menu(sports[choice])
                if choice == 0:
                    self.print_menu = False
                else:
                    print("Invalid input, please try again.")
                    self.menu()
            except ValueError:
                print("Press only numbers")
                exit_program = input(
                    "Please try again or press x to exit or press any key to continue: "
                )
                if exit_program.lower() == "x":
                    print("Exiting program...")
                    break

    def sub_menu(self, sports_choice):
        wipe_screen()
        self.print_sub_menu = True
        seasons = [
            f"{self.padding}{index + 1}. {season['year']}"
            for index, season in enumerate(sports_choice["seasons"])
        ]

        while self.print_sub_menu:
            print("Select a season to scrape:")
            print(*seasons, sep="\n")
            print(f"{self.padding}0. Go Back to Sports Menu")
            try:
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
                    self.print_sub_menu = False
                    self.menu()
                else:
                    print("Invalid input, please try again.")
                    self.sub_menu(sports_choice)
            except ValueError:
                print("Press only numbers")
                exit_program = input(
                    "Please try again or press x to exit or press any key to continue: "
                )
                if exit_program.lower() == "x":
                    print("Exiting program...")
                    quit()
