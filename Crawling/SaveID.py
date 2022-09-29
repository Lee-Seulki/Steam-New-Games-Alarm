import requests
from bs4 import BeautifulSoup

def collect_new_ids(id_list : str):
    '''
    스팀의 신규 제품 App Id를 수집하는 함수입니다.
    id_list = 'id_list의 파일 경로'
    ex) './id_list.txt'
    '''
    new_crawling_id = []
    URL = 'https://store.steampowered.com/search/results/?query&start=0&count=50&sort_by=Released_DESC&snr=1_7_7_popularnew_7&filter=popularnew&os=win&infinite=1'
    res = requests.get(URL, cookies={
        'Steam_Language':'koreana'
    })
    json_data = res.json()
    soup = BeautifulSoup(json_data['results_html'], 'html.parser')
    appids = soup.select('a')[:5]
    for appid in appids:
        idtag = appid.attrs['data-ds-appid']
        new_crawling_id.append(idtag)

    with open(id_list, 'r', encoding='utf-8') as f:
        id_list = f.readlines()
        global origin_id_list
        origin_id_list = []
        for id in id_list:
            temp = id.rstrip()
            origin_id_list.append(temp) 

    new_id = []
    for id in new_crawling_id:
        if id not in origin_id_list:
            new_id.append(id)
    return new_id

def update_id_list(new_id, update_id_list : str):
    '''
    기존의 ID List를 갱신합니다.
    new_id = 갱신된 app id값을 저장할 리스트
    update_id_list = 'id_list의 파일 경로'
    '''
    for id in origin_id_list:
        new_id.append(id)
    with open(update_id_list, 'w') as f:
        for id in new_id:
            f.write(id + '\n')
    return True