import json
import requests

def melon_search(query):
    params = {
        'jsoncallback' : '_',
        'query' : query,
    }
    jsonp_string = requests.get('http://www.melon.com/search/keyword/index.json', params = params).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')
    meta = json.loads(json_string)
    message = []

    if 'SONGCONETENTS' in meta:
        for song in meta['SONGCONTENTS']:
            message.append('''[{ALBUMNAME}] [{SONGNAME}] by {ARTISTNAME}
- http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))

    if message:
        message = '\n'.join(messages)
    else:
        message = '검색어 "{}"에 대한 노래 검색결과가 없습니다.'.format(query)

    return message
