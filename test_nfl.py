from functions import scrape_oddsportal_historical, scrape_page_typeA
from selenium import webdriver


global DRIVER_LOCATION
DRIVER_LOCATION = "/Usr/local/bin/chromedriver"
global TYPE_ODDS
TYPE_ODDS = "CLOSING"
global driver
driver = webdriver.Chrome(executable_path=DRIVER_LOCATION)


def nfl_2016():
    """
    Scrape the first 3 pages of the 2016 season of the NFL
    """

    # scrape_oddsportal_historical(
    #     sport="american-football",
    #     country="usa",
    #     league="nfl",
    #     start_season="2016-2017",
    #     current_season="no",
    #     max_page=3,
    # )
    import pdb

    pdb.set_trace()
    driver = webdriver.Chrome(executable_path=DRIVER_LOCATION)
    results, successes, fails = scrape_page_typeA(
        3, "american-football", "usa", "nfl", "2016-2017"
    )
    driver.close()
    print(results)
    print(f"ration of successes: {successes / (successes + fails)}")
    import pdb

    pdb.set_trace()
    pass


if __name__ == "__main__":
    nfl_2016()

# MISSING FROM CSV
# pre-season - this is probably intentional
# 9/8/16 - season opener
# 9/11/16
# 9/12 games are actually 9/11 games
# looks this is taking a brute force approach and hoping for the best
# maybe we can increase the amount of attempts and how long we wait for things
