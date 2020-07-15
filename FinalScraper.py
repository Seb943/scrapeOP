############ Final oddsportal scraper 

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
''' Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games'''
import os

os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *
#scrape_oddsportal_historical(sport = 'soccer', country = 'france', league = 'ligue-1', start = '2010-2011', nseason = 5, current_season = 'yes')
#scrape_oddsportal_current_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2020')
#scrape_oddsportal_specific_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2019', max_page = 2)
scrape_oddsportal_next_games(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2019')
