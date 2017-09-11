
import json
import requests
def melon_search(query):
    params = {
        'jscallback': '_',
        'query': query,
    }
    jsonp_string = requests.get('http://www.melon.com/search/keyword/index.json', params=params).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')

    meta = json.loads(json_string)
    messages = []
    if 'SONGCONTENTS' in meta:
        for song in meta['SONGCONTENTS']:
            messages.append('''[{ALBUMNAME}] {SONGNAME} by {ARTISTNAME} - http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))

    if messages:
        message = '\n'.join(messages)
    else:
        message = '검색어 "{}"에 대한 노래 검색결과가 없습니다.'.format(query)
    return message
