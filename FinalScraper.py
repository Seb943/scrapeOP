############ Final oddsportal scraper

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
''' Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games
NB : You need to be in the right repository to import functions...'''
import os

from functions import *

print('Data will be saved in the following directory:', os.getcwd())


scrape_oddsportal_historical(sport = 'soccer', country = 'france', league = 'ligue-1', start_season = '2020-2021', nseasons = 1, current_season = 'no', max_page = 1)

# scrape_oddsportal_current_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2020', max_page = 25)
# scrape_oddsportal_specific_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2019', max_page = 25)
# scrape_oddsportal_next_games(sport = 'tennis', country = 'germany', league = 'exhibition-bett1-aces-berlin-women', season = '2020')





