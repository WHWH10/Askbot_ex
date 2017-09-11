import json
from django.shortcuts import render
from .decorators import bot
from .import functions

@bot
def on_init(request):
    return {'type' : 'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content'] #photo 타입일 경우에는 이미지 URL

    if content.startswith('멜론검색:'):
        query = content[6:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)
    else:
        response = '지원하는 명령어가 아닙니다.'

    return {
        'message': {
            'text' : response,
        }
    }
    pass

@bot
def on_added(request):
    user_key = request.JSON['user_key']
    #pass

@bot
def on_block(request, user_key):
    pass

@bot
def on_leave(request, user_key):
    pass
