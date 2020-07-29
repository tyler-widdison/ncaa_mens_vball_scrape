#imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

#urls wanted
urls = ['https://www.ncaa.com/scoreboard/volleyball-men/d1/2019/12/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2019/12/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2019/12/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/01/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/02/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d1/2020/03/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2019/12/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2019/12/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2019/12/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/01/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/02/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d2/2020/03/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2019/12/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2019/12/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2019/12/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/30',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/01/31',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/11',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/12',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/13',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/14',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/15',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/16',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/17',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/18',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/19',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/20',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/21',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/22',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/23',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/24',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/25',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/26',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/27',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/28',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/02/29',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/01',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/02',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/03',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/04',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/05',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/06',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/07',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/08',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/09',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/10',
        'https://www.ncaa.com/scoreboard/volleyball-men/d3/2020/03/11']

#put match ids into a list

match_info = []
game_ids = []
date = []
for link in urls:
    try:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        div = soup.find('div', {'class': 'gamePod_content-pod_container'})
        for link in div.find_all('a', href=True):
            date.append(soup.find('div',{'class':'scoreboardDateNav-date selected hasGames'}).find('a')['href'][30:50])
            game_ids.append('https://www.ncaa.com' + link['href'])
        for a in div.find_all('div',{'class':'gamePod gamePod-type-game status-final'}):
            match_with_n = a.text
            tt = re.sub('\n+','\n',match_with_n)
            td = tt.replace('\n', ',')
            match_info.append(td)
    except:
        print(link)

dfs = pd.DataFrame(match_info)
df = pd.DataFrame(game_ids)
df['date'] = date
tt = df[0].str.split('/',4,expand=True).rename(columns={0:"a", 1:"a.5", 2:"b", 3:"c", 4:"d"})
tt['url'] = 'https://data.ncaa.com/casablanca/game/'
tt['url2'] = '/boxscore.json'
df['json_links'] = tt[['url', 'd', 'url2']].agg(''.join,axis=1).to_frame()
df = df.rename(columns={0:'match_link'})
df.to_csv('ncaa_m_links.csv')





#############################################################
#-----------------------------------------------------------#
#############################################################

import json
import csv
import urllib.request

df_links = pd.read_csv('ncaa_m_links.csv')
urls_2020 = []
with open('ncaa_m_links.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        urls_2020.append(row[3])


dfs = []
dfs2 = []
for u in urls_2020[1:]:   
    try:
        with urllib.request.urlopen(u) as url:
            data = json.loads(url.read().decode())
            match = data['meta']['description'].split('for ')[1]
            date = data['meta']['updatedTimestamp'].split(' ')[0]
            df_home_team = pd.DataFrame(data['teams'][0]['playerStats'])
            df_away_team = pd.DataFrame(data['teams'][1]['playerStats'])
            is_team_home_team = data['meta']['teams'][0]['homeTeam']
            is_team_home_team2 = data['meta']['teams'][1]['homeTeam']
            team = data['meta']['teams'][0]['seoName']
            opponent = data['meta']['teams'][1]['seoName']
            df = pd.DataFrame(df_home_team).assign(match=match, date=date, team=opponent, opponent=team, is_team_home_team=is_team_home_team2, u=u)
            df2 = pd.DataFrame(df_away_team).assign(match=match, date=date, team=team, opponent=opponent, is_team_home_team=is_team_home_team, u=u)
            dfs.append(df)
            dfs2.append(df2)
    except:
        continue

df_fin_home = pd.concat(dfs)
df_fin_away = pd.concat(dfs2)
df = pd.concat([df_fin_home, df_fin_away])
df.to_csv('men_2020_box_scores.csv')
