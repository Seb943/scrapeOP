############ Final oddsportal scraper 

# ATP, baseball, basket, darts, eSports, football, nfl, nhl, rugby
''' Create three main functions : scrape_historical, scrape current_season, scrape_next_games'''

from functions import *
#scrape_oddsportal_historical(sport = 'soccer', country = 'france', league = 'ligue-1', start = '2010-2011', nseason = 5, current_season = 'yes')
scrape_oddsportal_current_season(sport = 'soccer', country = 'france', league = 'ligue-1', season = '2019-2020')
scrape_oddsportal_next_games(sport = 'soccer', country = 'france', league = 'ligue-1', season = '2019-2020')