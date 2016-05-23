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
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            with open('cookies/'+account+'.json','w') as f:
                json.dump(cookie, f, ensure_ascii=False, indent = 4)
        else:
            print "Failed!( Reason:%s )" % info['reason']
    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)
