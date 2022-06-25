############ Final oddsportal scraper

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
""" Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games
NB : You need to be in the right repository to import functions..."""
import os
import json

# os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *

print("Data will be saved in the following directory:", os.getcwd())

sports = {
    1: {
        "sport": "american-football",
        "country": "usa",
        "league": "nfl",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
            {"year": "2009-2010", "pages": 7},
            {"year": "2010-2011", "pages": 7},
            {"year": "2011-2012", "pages": 7},
            {"year": "2012-2013", "pages": 7},
            {"year": "2013-2014", "pages": 7},
            {"year": "2014-2015", "pages": 7},
            {"year": "2015-2016", "pages": 7},
            {"year": "2016-2017", "pages": 7},
            {"year": "2017-2018", "pages": 7},
            {"year": "2018-2019", "pages": 7},
            {"year": "2019-2020", "pages": 7},
            {"year": "2020-2021", "pages": 6},
            {"year": "2021-2022", "pages": 7},
        ],
    },
    2: {
        "sport": "hockey",
        "country": "usa",
        "league": "nhl",
        "seasons": [
            {"year": "2003-2004", "pages": 10},
            {"year": "2005-2006", "pages": 11},
            {"year": "2006-2007", "pages": 11},
            {"year": "2007-2008", "pages": 11},
            {"year": "2008-2009", "pages": 11},
            {"year": "2009-2010", "pages": 11},
            {"year": "2010-2011", "pages": 11},
            {"year": "2011-2012", "pages": 11},
            {"year": "2012-2013", "pages": 11},
            {"year": "2013-2014", "pages": 11},
            {"year": "2014-2015", "pages": 11},
            {"year": "2015-2016", "pages": 11},
            {"year": "2016-2017", "pages": 11},
            {"year": "2017-2018", "pages": 11},
            {"year": "2018-2019", "pages": 11},
            {"year": "2019-2020", "pages": 11},
            {"year": "2020-2021", "pages": 11},
            {"year": "2021-2022", "pages": 11},
        ],
    },
    3: {
        "sport": "baseball",
        "country": "usa",
        "league": "mlb",
        "seasons": [
            {"year": "2006", "pages": 11},
            {"year": "2007", "pages": 11},
            {"year": "2008", "pages": 11},
            {"year": "2009", "pages": 11},
            {"year": "2010", "pages": 11},
            {"year": "2011", "pages": 11},
            {"year": "2012", "pages": 11},
            {"year": "2013", "pages": 11},
            {"year": "2014", "pages": 11},
            {"year": "2015", "pages": 11},
            {"year": "2016", "pages": 11},
            {"year": "2017", "pages": 11},
            {"year": "2018", "pages": 11},
            {"year": "2019", "pages": 11},
            {"year": "2020", "pages": 11},
            {"year": "2021", "pages": 11},
            {"year": "2022", "pages": 11},
        ],
    },
    4: {
        "sport": "soccer",
        "country": "usa",
        "league": "mls",
        "seasons": [
            {"year": "2004", "pages": 4},
            {"year": "2005", "pages": 4},
            {"year": "2006", "pages": 5},
            {"year": "2007", "pages": 5},
            {"year": "2008", "pages": 5},
            {"year": "2009", "pages": 5},
            {"year": "2010", "pages": 6},
            {"year": "2011", "pages": 7},
            {"year": "2012", "pages": 7},
            {"year": "2013", "pages": 7},
            {"year": "2014", "pages": 7},
            {"year": "2015", "pages": 8},
            {"year": "2016", "pages": 8},
            {"year": "2017", "pages": 8},
            {"year": "2018", "pages": 9},
            {"year": "2019", "pages": 9},
            {"year": "2020", "pages": 6},
            {"year": "2021", "pages": 10},
            {"year": "2022", "pages": 5},
        ],
    },
    5: {
        "sport": "soccer",
        "country": "japan",
        "league": "Japanese J1",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    6: {
        "sport": "soccer",
        "country": "australia",
        "league": "Australian A-League",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    7: {
        "sport": "soccer",
        "country": "Brazil",
        "league": "Brazilian Series A",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    8: {
        "sport": "soccer",
        "country": "england",
        "league": "English Premier",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    9: {
        "sport": "soccer",
        "country": "england",
        "league": "English League Championship",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    10: {
        "sport": "soccer",
        "country": "englad",
        "league": "English League One",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    11: {
        "sport": "soccer",
        "country": "engald",
        "league": "English League Two",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    12: {
        "sport": "soccer",
        "country": "sweden",
        "league": "Swedish Allsvenskan",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    13: {
        "sport": "soccer",
        "country": "france",
        "league": "French League One",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    14: {
        "sport": "soccer",
        "country": "italy",
        "league": "Italy Series A",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    15: {
        "sport": "soccer",
        "country": "spain",
        "league": "Spanish Premier",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
    16: {
        "sport": "soccer",
        "country": "mexico",
        "league": "Mexico MX",
        "seasons": [
            {"year": "2008-2009", "pages": 6},
        ],
    },
}

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
