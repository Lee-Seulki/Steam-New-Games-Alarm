from SaveID import collect_new_ids, update_id_list
from SteamCrwaling import new_games_crawling
import telegram
import os
import pathlib
from datetime import datetime

os.chdir(pathlib.Path(__file__).parent.absolute())
# currentPath = os.getcwd()
now = datetime.now()
print('전송완료 '+ str(now.month)+ '/' +str(now.day))

telegram_config = {}
with open('telegram_config', 'r', encoding='utf-8') as f:
    configs = f.readlines()
    for config in configs:
        key, value = config.rstrip().split('=')
        telegram_config[key] = value
token = telegram_config['token']

new_id = collect_new_ids('id_list/id_list.txt')
new_games = new_games_crawling(new_id)

bot = telegram.Bot(token)

if new_id == []:
    bot.send_message(telegram_config['my_chat_id'], '신제품이 없습니다.')

else:
    msg = ''
    for tt, req in new_games.items():
        reqst = ''
        for r in req:
            reqst += r + '\n'
        msg += tt + '\n' + reqst + '\n'
    bot.send_message(telegram_config['my_chat_id'], msg)

update_id_list(new_id, 'id_list/id_list.txt')