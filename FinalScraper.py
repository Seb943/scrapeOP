############ Final oddsportal scraper 

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
''' Create 4 main functions : scrape_historical, scrape_specific_season, scrape current_season, scrape_next_games'''
import os

#os.chdir("C:\\Users\\Sébastien CARARO\\Desktop\\ATP& &Others\\WebScraping")
from functions import *

print('Data will be saved in the following directory:', os.getcwd())


#scrape_oddsportal_historical(sport = 'soccer', country = 'france', league = 'ligue-1', start_season = '2010-2011', nseasons = 5, current_season = 'yes', max_page = 25)
#scrape_oddsportal_current_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2020', max_page = 25)
#scrape_oddsportal_specific_season(sport = 'soccer', country = 'finland', league = 'veikkausliiga', season = '2019', max_page = 25)
#scrape_oddsportal_next_games(sport = 'tennis', country = 'germany', league = 'exhibition-bett1-aces-berlin-women', season = '2020')

scrape_oddsportal_historical(sport = 'basketball', country = 'china', league = 'cba', start_season = '2011-2012', nseasons = 1, current_season = 'yes', max_page = 2)
scrape_oddsportal_historical(sport = 'baseball', country = 'south-korea', league = 'kbo', start_season = '2013', nseasons = 1, current_season = 'yes', max_page = 2)
scrape_oddsportal_historical(sport = 'hockey', country = 'usa', league = 'nhl', start_season = '2012-2013', nseasons = 1, current_season = 'yes', max_page = 2)
scrape_oddsportal_historical(sport = 'soccer', country = 'usa', league = 'mls', start_season = '2013', nseasons = 1, current_season = 'yes', max_page = 2)




