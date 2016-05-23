# encoding=utf-8
import json
import base64
import requests


myWeiBo = [
    {'no': '403519445@qq.com', 'psw': 'mxx403519445'},
    {'no': 'shudieful3618@163.com', 'psw': 'a123456'},
    {'no': 'yuejiamouwei07@163.com', 'psw': 'aaa333'},
    {'no': 'yuequ26463917@163.com', 'psw': 'aaa333'},
    {'no': 'yuejiao4881241@163.com', 'psw': 'aaa333'},
    {'no': 'yueshanre1265@163.com', 'psw': 'aaa333'},
    {'no': 'yuesibi2671@163.com', 'psw': 'aaa333'},
    {'no': 'laoxia6168867@163.com', 'psw': 'aaa333'},
    {'no': 'laoxian89860163@163.com', 'psw': 'aaa333'},
    {'no': 'laoxiebo63@163.com', 'psw': 'aaa333'},
    {'no': 'laoyan5554443@163.com', 'psw': 'aaa333'},
    {'no': 'laoye00077381109@163.com', 'psw': 'aaa333'},
    {'no': 'lashiyongmei5488@163.com', 'psw': 'aaa333'},
    {'no': 'latuozhaomou8@163.com', 'psw': 'aaa333'},
    {'no': 'layeshi43441014@163.com', 'psw': 'aaa333'},
    {'no': 'ledan9775@163.com', 'psw': 'aaa333'},
    {'no': 'ledao347874534@163.com', 'psw': 'aaa333'},
    {'no': 'leidun77839@163.com', 'psw': 'aaa333'},
    {'no': 'leigao9970795099@163.com', 'psw': 'aaa333'},
    {'no': 'leihaoyi2@163.com', 'psw': 'aaa333'},
    {'no': 'leilueshi7227@163.com', 'psw': 'aaa333'},
    {'no': 'leimu5505@163.com', 'psw': 'aaa333'},
    {'no': 'leishi4826609@163.com', 'psw': 'aaa333'},
    {'no': 'leizongcuqiao4@163.com', 'psw': 'aaa333'},
    {'no': 'lhjj5384642@163.com', 'psw': 'aaa333'},
    {'no': 'lhwa9035991@163.com', 'psw': 'aaa333'},
    {'no': 'li6641086665909@163.com', 'psw': 'aaa333'},
    {'no': 'li93348947990288@163.com', 'psw': 'aaa333'},
    {'no': 'lian2997275557@163.com', 'psw': 'aaa333'},
    {'no': 'lian5718783@163.com', 'psw': 'aaa333'},
    {'no': 'liandangxingliao@163.com', 'psw': 'aaa333'},
    {'no': 'liandou59061@163.com', 'psw': 'aaa333'},
    {'no': 'lianfang1691862@163.com', 'psw': 'aaa333'},
    {'no': 'liang04685@163.com', 'psw': 'aaa333'},
    {'no': 'liang58803@163.com', 'psw': 'aaa333'},
    {'no': 'lianggang402465@163.com', 'psw': 'aaa333'},
    {'no': 'liangjingmaopo37@163.com', 'psw': 'aaa333'},
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    for elem in weibo:
        with open('cookies/'+elem['no']+'.json','r') as f:
            cookie = json.load(f)
        print "Get Cookie Success!( Account:%s )" % elem['no']
        cookies.append(cookie)
    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)
