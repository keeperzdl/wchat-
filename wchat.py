#!/usr/bin/env.python
# -*- coding: utf-8 -*-

import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply+"[I'm a robot. Talk to me. Talk on the phone]"

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
def tuling_reply(msg):
    group = itchat.get_chatrooms(update=True)
    for g in group:
        if g['NickName'] == u"Java狼人杀交流忽悠群":
            from_group = g['UserName']
            if msg['FromUserName'] == from_group or msg['FromUserName'] == u"夜袭寡妇村":
                defaultReply = 'I received: ' + msg['Text']
                reply = get_response(msg['Text'])
                return reply or defaultReply+"[I'm a robot. Talk to me. Talk on the phone]"

# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=True)
itchat.auto_login()
itchat.run()

#@0fe5213674830cf9f9bc9d218da1cf1ce7d7a54426ff43415bfb34a939d387f8