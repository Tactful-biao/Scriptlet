import re
import base64
import json

ssr = input('请输入ssr:后的部分:')

ssr_data = str(base64.urlsafe_b64decode(ssr+'=='), 'utf-8')
data = re.search('(.*):(\d+):(.*):(.*):(.*):(.*)', ssr_data)

config = {
    "server": "0.0.0.0",
    "server_ipv6": "::",
    "server_port": 8300,
    "local_address": "127.0.0.1",
    "local_port": 1080,

    "password": "password",
    "method": "chacha20",
    "protocol": "origin",
    "protocol_param": "",
    "obfs": "plain",
    "obfs_param": "",
    "speed_limit_per_con": 0,
    "speed_limit_per_user": 0
}

pwd = re.search('(.*?)\/\?', data.group(6)).group(1)

config['server'] = data.group(1)
config['server_port'] = data.group(2)
config['protocol'] = data.group(3)
config['method'] = data.group(4)
config['obfs'] = data.group(5)
config['password'] = str(base64.urlsafe_b64decode(pwd + '=='), 'utf-8')
# config['protocol_param'] = data.group()
# config['obfs_param'] = ''

with open('shadow.json', 'w') as j:
    j.write(json.dumps(config))
