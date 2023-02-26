# Create clean scraped table 
# encoding : 'utf-8'
# python 3.6
import numpy as np
import pandas as pd
import os 

print(os.getcwd())
def create_clean_table_two_ways(df):
  # (a) Count the number of bookmakers
  nbooks = df['Bookmaker'].nunique()
  
  # (b) Assign a number to each game
  L = [0 for i in range(df['Bookmaker'].size)]
  for i in range(1,df['Bookmaker'].size):
    if (df['Date'][i] != df['Date'][i-1]) | (df['Home_id'][i] != df['Home_id'][i-1]) | (df['Away_id'][i] != df['Away_id'][i-1]):
      L[i] = 1

  df['MatchId'] = np.cumsum(L) + 1

  # (c) Create final dataframe containing only one line per match
  df_final = pd.DataFrame(index=range(max(df['MatchId'])), columns=range(7)) #  Home_id, Away_id, Date, Score_home, Score_away, Season, MatchId
  df_final.columns = ['MatchId','Season','Home_id', 'Away_id', 'Date', 'Score_home', 'Score_away']
  c = 0
  for book in df['Bookmaker'].unique():
    print(book)
    df_final['{}_H'.format(book)] = 'Na' # Home victory odds
    df_final['{}_A'.format(book)] = 'Na' # Away victory odds
    for id in range(1, max(df['MatchId']) + 1):
      new_df = df[(df['Bookmaker'] == book) & (df['MatchId'] == id)]
      if new_df.shape[0] > 0:
        #print(id)
        df_final['{}_H'.format(book)].iloc[id-1] = new_df['OddHome'].iloc[0]
        df_final['{}_A'.format(book)].iloc[id-1] = new_df['OddAway'].iloc[0]
        df_final['MatchId'].iloc[id-1] = new_df['MatchId'].iloc[0]
        df_final['Season'].iloc[id-1] = new_df['Season'].iloc[0]
        df_final['Home_id'].iloc[id-1] = new_df['Home_id'].iloc[0]
        df_final['Away_id'].iloc[id-1] = new_df['Away_id'].iloc[0]
        df_final['Date'].iloc[id-1] = new_df['Date'].iloc[0]
        df_final['Score_home'].iloc[id-1] = new_df['Score_home'].iloc[0]
        df_final['Score_away'].iloc[id-1] = new_df['Score_away'].iloc[0]
    c+=1
    
  try : 
    days = df_final['Date'].str[:2]
    months = df_final['Date'].str[3:6]
    years = df_final['Date'].str[7:]
    months[months == 'Jan'] = '01'
    months[months == 'Feb'] = '02'
    months[months == 'Mar'] = '03'
    months[months == 'Apr'] = '04'
    months[months == 'May'] = '05'
    months[months == 'Jun'] = '06'
    months[months == 'Jul'] = '07'
    months[months == 'Aug'] = '08'
    months[months == 'Sep'] = '09'
    months[months == 'Oct'] = '10'
    months[months == 'Nov'] = '11'
    months[months == 'Dec'] = '12'
    date = days + '/' + months + '/' + years
    df_final['Date'] = pd.to_datetime(date, format='%d/%m/%Y')
    df.sort_values(by=['Date'])
  except:
    print('Cannot convert Date into regular Date format')

  return(df_final)

def create_clean_table_three_ways(df):
  # (a) Count the number of bookmakers
  nbooks = df['Bookmaker'].nunique()
  
  # (b) Assign a number to each game
  L = [0 for i in range(df['Bookmaker'].size)]
  for i in range(1,df['Bookmaker'].size):
    if (df['Date'][i] != df['Date'][i-1]) | (df['Home_id'][i] != df['Home_id'][i-1]) | (df['Away_id'][i] != df['Away_id'][i-1]):
      L[i] = 1

  df['MatchId'] = np.cumsum(L) + 1

  # (c) Create final dataframe containing only one line per match
  df_final = pd.DataFrame(index=range(max(df['MatchId'])), columns=range(7)) #  Home_id, Away_id, Date, Score_home, Score_away, Season, MatchId
  df_final.columns = ['MatchId','Season','Home_id', 'Away_id', 'Date', 'Score_home', 'Score_away']
  c = 0
  for book in df['Bookmaker'].unique():
    print(book)
    df_final['{}_H'.format(book)] = 'Na' # Home victory odds
    df_final['{}_D'.format(book)] = 'Na' # Draw odds
    df_final['{}_A'.format(book)] = 'Na' # Away victory odds
    for id in range(1, max(df['MatchId']) + 1):
      new_df = df[(df['Bookmaker'] == book) & (df['MatchId'] == id)]
      if new_df.shape[0] > 0:
        #print(id)
        df_final['{}_H'.format(book)].iloc[id-1] = new_df['OddHome'].iloc[0]
        df_final['{}_D'.format(book)].iloc[id-1] = new_df['OddDraw'].iloc[0]
        df_final['{}_A'.format(book)].iloc[id-1] = new_df['OddAway'].iloc[0]
        df_final['MatchId'].iloc[id-1] = new_df['MatchId'].iloc[0]
        df_final['Season'].iloc[id-1] = new_df['Season'].iloc[0]
        df_final['Home_id'].iloc[id-1] = new_df['Home_id'].iloc[0]
        df_final['Away_id'].iloc[id-1] = new_df['Away_id'].iloc[0]
        df_final['Date'].iloc[id-1] = new_df['Date'].iloc[0]
        df_final['Score_home'].iloc[id-1] = new_df['Score_home'].iloc[0]
        df_final['Score_away'].iloc[id-1] = new_df['Score_away'].iloc[0]
    c+=1
    
  try : 
    days = df_final['Date'].str[:2]
    months = df_final['Date'].str[3:6]
    years = df_final['Date'].str[7:]
    months[months == 'Jan'] = '01'
    months[months == 'Feb'] = '02'
    months[months == 'Mar'] = '03'
    months[months == 'Apr'] = '04'
    months[months == 'May'] = '05'
    months[months == 'Jun'] = '06'
    months[months == 'Jul'] = '07'
    months[months == 'Aug'] = '08'
    months[months == 'Sep'] = '09'
    months[months == 'Oct'] = '10'
    months[months == 'Nov'] = '11'
    months[months == 'Dec'] = '12'
    date = days + '/' + months + '/' + years
    df_final['Date'] = pd.to_datetime(date, format='%d/%m/%Y')
    df.sort_values(by=['Date'])
  except:
    print('Cannot convert Date into regular Date format')

  return(df_final)
  

def create_clean_df(fileloc, sep = ";", ways = 2):
  df = pd.read_csv(fileloc + '.csv', sep = sep)
  if ways == 2:
    df = create_clean_table_two_ways(df)
  if ways == 3:
    df = create_clean_table_three_ways(df)
  
  df.to_csv(fileloc +'_CLEAN' +  '.csv', index = False)
  print('Finished cleaning table!')
  return(0)
  
