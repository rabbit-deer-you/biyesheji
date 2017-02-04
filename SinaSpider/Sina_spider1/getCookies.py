# encoding=utf-8
import json
import base64
import requests


myWeiBo = [
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
