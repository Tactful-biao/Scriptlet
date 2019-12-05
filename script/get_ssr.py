import requests
import random
import time
import re
from bs4 import BeautifulSoup


s = requests.Session()
mail = ''

# 邮件内容地址加密串
eml = ''

DOMAIN = 'https://xxjc.me/'


def get_cookies():
    '''获取cookies'''
    url = 'http://mail.bccto.me/'
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Host': 'mail.bccto.me',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://mail.bccto.me',
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Upgrade-Insecure-Requests': '1'
    }
    s.get(url, headers=headers)


def get_mail_address():
    '''获取邮箱地址'''
    url = 'http://mail.bccto.me/applymail'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '26',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'mail.bccto.me',
        'Origin': 'http://mail.bccto.me',
        'Referer': 'http://mail.bccto.me/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    global mail

    # 随机取一个邮箱去注册
    mail = str(random.randrange(1000000, 99999999999)) + random.choice(['@bccto.me', '@chaichuang.com', '@jnpayy.com', '@3202.com', '@eaek.cc', '@4057.com', '@huaweimali.cn', '@juyouxi.com', '@hotmali.cn', '@dawin.com', '@a7996.com'])
    data = {'mail': mail}
    s.post(url, headers=headers, data=data)
    print('随机邮箱地址为: ' + mail)


def register():
    '''模拟发送邮件
    获取邮件内容
    注册ssr'''
    ss = requests.Session()
    ck = ss.get(DOMAIN).cookies
    cookie = re.search('\s(.*=.*?)\s', str(ck)).group(1) + ';'

    # 给获取的邮箱发送验证码
    url = DOMAIN + 'auth/send'
    headers = {
        'Origin': DOMAIN,
        'Referer': DOMAIN + 'auth/register',
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {'email': mail}
    ss.post(url, headers=headers, data=data)
    print('正在发送验证码中...')

    # 监控是否收到验证码
    get_mail_notice()

    # 注册地址
    register_url = DOMAIN + 'auth/register'

    datas = {
        'email': mail,
        'name': mail,
        'passwd': mail,
        'repasswd': mail,
        'wechat': str(random.randrange(10000, 1000000000)),
        'imtype': '2',
        'code': '0',
        'emailcode': get_mail_text()
    }
    ss.post(register_url, headers=headers, data=datas)
    print('注册完成！')


def get_mail_notice():
    '''判断是否收到邮件'''
    url = 'http://mail.bccto.me/getmail'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '61',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'mail.bccto.me',
        'Origin': 'http://mail.bccto.me',
        'Referer': 'http://mail.bccto.me/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'mail': mail,
        'time': str(int(time.time())),
        '_': str(int(float(time.time()*1000)))
    }
    print('开始等待验证码到来，请稍等...')
    while True:
        res = s.post(url, headers=headers, data=data).json()
        if res.get('mail'):
            break

    global eml
    eml = res['mail'][0][4]


def get_mail_text():
    '''获取邮件具体内容'''
    print('正在提取验证码内容...')
    # 取邮箱前半部分
    mail_name = re.search('\d+', mail).group(0)

    # 取邮箱的域名部分
    mail_domain = re.search('@(.*)', mail).group(1).replace('.', '-_-')

    # 构造邮件具体内容地址
    url = 'http://mail.bccto.me/win/'+mail_name+'(a)'+mail_domain+'/' + eml

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'mail.bccto.me',
        'Referer': 'http://mail.bccto.me/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    content = s.get(url, headers=headers).text

    # 提取验证码
    yzm = re.search('您的邮箱验证代码为.*(\d{6})', content)
    if yzm:
        return yzm.group(1)
    else:
        print('没有获取的验证码内容！请重新尝试！')


def login():
    '''
    模拟登录
    :return:
    '''
    print('登录中...')
    sss = requests.Session()
    url = DOMAIN + 'auth/login'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': DOMAIN,
        'Referer': DOMAIN + 'auth/login',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'email': mail,
        'passwd': mail,
        'code': ''
    }

    header = {
        'referer': DOMAIN+'user/node',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    sss.post(url, headers=headers, data=data)

    with open('/home/bao/mx.json', 'w', encoding='utf-8') as mx:
        res = sss.get(DOMAIN + 'user').text
        link = re.search('(https://xxjcdy.club/link/.*?)"', res).group(1)
        print(link)
        mx.write(mail + '\n' + link + '\n')
        
        # 签到领流量
        checkin = DOMAIN + 'user/checkin'
        checkined = sss.post(checkin, headers=headers).text
        print(checkined)
        
        node = DOMAIN + 'user/node'

        node_data = sss.get(node).text

        soup = BeautifulSoup(node_data, 'lxml')

        vip_node = soup.find('div', {'id': 'cardgroup1'})

        node_nums = re.findall("urlChange\('(\d+)'", str(vip_node))
        # print(node_nums)
        
        # 获取ssr数据和ssr链接
        for i in node_nums:
            ssr_url = DOMAIN + 'user/node/'+i+'?ismu=80&relay_rule=0'
            res = sss.get(ssr_url, headers=header).text

            soup = BeautifulSoup(res, 'lxml')
            ssr_data = soup.find('pre')
            if ssr_data:
                print(ssr_data.getText())
                mx.write(ssr_data.getText() + '\n')
                ssr_link = re.search("'(ssr:.*?)'", res).group(1)
                print(ssr_link)
                mx.write(ssr_link + '\n')
                print('*'*30)


if __name__ == '__main__':
    get_cookies()
    get_mail_address()
    register()
    login()
