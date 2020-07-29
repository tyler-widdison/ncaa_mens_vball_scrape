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
match_ids = []
for u in urls:
    try:
        r = requests.get(u)
        soup = BeautifulSoup(r.content)
        link1 = soup.find('a',{'class':'gamePod-link'})['href']
        link = 'https://www.ncaa.com' + link1
        match_ids.append(link)
    except:
        continue

df_boxscore_links = pd.DataFrame(match_ids)