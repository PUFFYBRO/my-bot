import vk_api
import time

vk = vk_api.VkApi (token='8fc4b916e04d68a0529481442070d33ed23701143f360a4bf365313dcb0d22f5baeffb6d7ecaffdedb43f')

values = {'out':0, 'count':100, 'time_offset':60}


while True:
    mes = vk.method('messages.getConversations',{'offset':0, 'count': 100, 'filter': 'unread'})
    if mes['count'] >=1:
        id = mes['items'][0]['last_message']['from_id']
        body = mes['items'][0]['last_message']['text']
        if body.lower() == 'привет':
            vk.method('messages.send',{'peer_id':id,'message': 'Привет, я Джимии, если хочешь узнать что я умею напиши слово "Команды"'})
        elif body.lower() == 'что ты умеешь?':
            vk.method('messages.send', {'peer_id': id, 'message': 'Я пока еще только учусь что-либо делать ;)'})
        elif body.lower() == 'команды':
            vk.method('messages.send', {'peer_id': id, 'message': 'Мои команды: Привет, Что ты умеешь?, Как у тебя дела?, Пока'})
        elif body.lower() == 'как у тебя дела?':
            vk.method('messages.send', {'peer_id': id, 'message': 'Все просто замечательно!'})
            vk.method('messages.send', {'peer_id': id, 'message': 'как у тебя?!'})
        elif body.lower() == 'пока':
            vk.method('messages.send', {'peer_id': id, 'message': 'Пока, буду тебя ждать)'})
        elif body.lower() == 'нормально':
            vk.method('messages.send', {'peer_id': id, 'message': 'Вот и славненько!)'})
        elif body.lower() == 'плохо':
            vk.method('messages.send', {'peer_id': id, 'message': 'Не грусти, все будет хорошо!'})
        elif body.lower() == 'ужасно':
            vk.method('messages.send', {'peer_id': id, 'message': 'Не грусти, все будет хорошо!'})
        elif body.lower() == 'замечательно':
            vk.method('messages.send', {'peer_id': id, 'message': 'Мне нравится твой оптимистичный настрой :)'})
        elif body.lower() == 'начать':
            vk.method('messages.send', {'peer_id': id, 'message': 'Привет, я Джимии, если хочешь узнать что я умею напиши слово "Команды"'})
        elif body.lower() == 'хай':
            vk.method('messages.send', {'peer_id': id, 'message': 'Привет, я Джимии, если хочешь узнать что я умею напиши слово "Команды"'})
        elif body.lower() == 'как ты?':
            vk.method('messages.send', {'peer_id': id, 'message': 'Я, как всегда хорошо'})
            vk.method('messages.send', {'peer_id': id, 'message': 'Ты как?'})
        elif body.lower() == 'хорошо':
            vk.method('messages.send', {'peer_id': id, 'message': 'Вот и славненько!)'})
        elif body.lower() == 'пидор':
            vk.method('messages.send', {'peer_id': id, 'message': 'Не стоит обзываться!(от пидора слышу)'})
        elif body.lower() == 'хуй':
            vk.method('messages.send', {'peer_id': id, 'message': 'Не стоит обзываться!(от хуеплета слышу)'})
        elif body.lower() == 'сука':
            vk.method('messages.send', {'peer_id': id, 'message': 'Не стоит обзываться!(от суки слышу)'})
        elif body.lower() == 'заебал':
            vk.method('messages.send', {'peer_id': id, 'message': 'Этого я и добивался ;)'})
        else:
            vk.method('messages.send', {'peer_id': id, 'message': 'Я тебя не понимаю:('})

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
         d[(-1, j)] = j + 1
    for i in range(lenstr1):
     for j in range(lenstr2):
         if s1[i] == s2[j]:
             cost = 0
    else:
        cost = 1
    d[(i, j)] = min(
    d[(i - 1, j)] + 1, # deletion
    d[(i, j - 1)] + 1, # insertion
    d[(i - 1, j - 1)] + cost, # substitution
)
    if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
        d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost) # transposition
    return d[lenstr1 - 1, lenstr2 - 1]
