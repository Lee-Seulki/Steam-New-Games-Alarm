from typing import List
import requests
from bs4 import BeautifulSoup

def new_games_crawling(new_id : List):
    '''
    신규 제품의 정보를 수집합니다.
    '''
    sysreqlist = {}
    for i in range(len(new_id)):
        appidURL = 'https://store.steampowered.com/app/' + new_id[i]
        res = requests.get(appidURL, cookies={
            'Steam_Language':'koreana'
        })
        soup = BeautifulSoup(res.text, 'html.parser')

        sysreq_content = soup.select_one('.game_area_sys_req.sysreq_content.active[data-os="win"]')
        if sysreq_content.select_one('.game_area_sys_req_leftCol') == None:
            sysreqs = sysreq_content.select('.game_area_sys_req_full li')
        else:
            sysreqs = sysreq_content.select('.game_area_sys_req_leftCol li')

        appName = soup.select_one('#appHubAppName').text
        release_date = soup.select_one('.release_date .date').text
        genre = soup.select('.glance_tags.popular_tags a')[0].text.strip()

        title = release_date + '\n<' + appName + ' (' + genre + ')>'
        
        req_list = []
        for sysreq in sysreqs:
            if '필요합니다' in sysreq.text:
                continue
            elif '추가 사항' in sysreq.text:
                continue
            else:
                req = sysreq.text.strip()
                req_list.append(req)
        sysreqlist[title] = req_list
    return sysreqlist