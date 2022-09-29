import requests
from bs4 import BeautifulSoup
'''
맨 처음에만 실행하는 파일입니다.
기존의 게임 목록들의 app id를 불러오기 위한 파이썬 파일입니다.
'''
id_list = []
for start in range(0, 451, 50):
    URL = 'https://store.steampowered.com/search/results/?query&start='+str(start)+'&count=50&sort_by=Released_DESC&snr=1_7_7_popularnew_7&filter=popularnew&os=win&infinite=1'
    res = requests.get(URL, cookies={
        'Steam_Language':'koreana'
    })
    json_data = res.json()
    soup = BeautifulSoup(json_data['results_html'], 'html.parser')
    appids = soup.select('a')
    
    for appid in appids:
        idtag = appid.attrs['data-ds-appid']
        id_list.append(idtag)

with open('id_list/id_list.txt', 'w') as f:
    for id in id_list:
        f.write(id + '\n')  