import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests

#############################################################
#-----------------------------------------------------------#
#############################################################

# get box score links from date links csv
df_date = pd.read_csv('ncaa_m_vball_date_links.csv')

url = df_date['link'][1:3] # only 2 links for testing. Remove the 3 to get everything

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
