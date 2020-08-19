import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests

#############################################################
#-----------------------------------------------------------#
#############################################################

# get box score links from date links csv
df_date = pd.read_csv('ncaa_m_vball_date_links.csv')

url = df_date['link'][0:]

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

links = []
for u in url:
    try:
        r = requests.get(u)
        soup = BeautifulSoup(r.content)
        for a in soup.find_all('a', href=True):
            if a.text:
                links.append(a['href'])
    except:
        print(u)

k = [k for k in links if 'box_score' in k]
kt = set(k)
df = pd.DataFrame(kt)
tt = df
tt['url'] = 'https://stats.ncaa.org'
df = tt[['url', 0]].agg(''.join,axis=1).to_frame()

df.to_csv('ncaa_m_vball_box_score_links.csv')


#############################################################
#-----------------------------------------------------------#
#############################################################


df_links = pd.read_csv('ncaa_m_vball_box_score_links.csv')

#url = df_links['0']

df_home_team = []
df_away_team = []
for u in df_links['0']:
    try:
        res = requests.get(u)
        soup = BeautifulSoup(res.text, 'html.parser')
        home_team_set_wins = pd.read_html(res.content, header = 0)[0]['Total'].values[0]
        away_team_set_wins = pd.read_html(res.content, header = 0)[0]['Total'].values[1]
        home_team = soup.find_all('a', {'class':'skipMask'})[1].text.strip()
        away_team = soup.find_all('a', {'class':'skipMask'})[0].text.strip()
        date = soup.find_all('table',{'align':'center'})[2].text.strip().split('\n')[2].strip()
        location = soup.find_all('table',{'align':'center'})[2].text.strip().split('Location:')[1].split('\n')[1]
        df_home_team.append(pd.read_html(res.content, header = 1)[3][:-1].assign(ncaa_match_id=u,team = away_team,team_set_wins=home_team_set_wins,opponent=home_team,date=date,match_location=location))
        df_away_team.append(pd.read_html(res.content, header = 1)[4][:-1].assign(ncaa_match_id=u,team = home_team,team_set_wins=away_team_set_wins,opponent=away_team,date=date,match_location=location))
    except:
        continue
    
df2 = pd.concat(df_home_team)
df1 = pd.concat(df_away_team)
df = pd.concat([df2, df1])
df.to_csv('men_2016-2020_box_scores.csv')
