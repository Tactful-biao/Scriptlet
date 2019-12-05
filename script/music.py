import requests
from Crypto.Cipher import AES
import base64
import re
from multiprocessing.pool import Pool


class Netease(object):
  def __init__(self, uid):
    self.uid = uid
    self.comments = list()
    self.encSecKey = '48a9661615fa0502afdcd25020d2add36961a23e8fa5c6705c4e4b9620f2b338331405db1d6d73ffe498729c8f4f0f97d334f2f662ac02191dc81b7ea455ef0bce48c78c579082f0f6c02e6f386f6cb1f1c22c4240954855fa3dfa9929ae081932813743362b26c5de258e349e8d73ebcc9d6e78275cbd4bf872616ee1c283bb'
    self.key = '0CoJUm6Qyw8W8jud'
    self.headers = {
      'origin': 'https://music.163.com',
      'Cookie': 'appver=1.5.0.75771;',
      'Referer': 'http://music.163.com/',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

  def getTopMusic(self):
    # 获取最近最喜欢听得100首歌曲
    url = 'https://music.163.com/weapi/v1/play/record?csrf_token='

    text = '{uid: "'+self.uid+'", type: "-1"}'

    data = {
      'params': str(self.get_params(self.key, text), 'utf-8'),
      'encSecKey': self.encSecKey
    }
    res = requests.post(url, headers=self.headers, data=data).text
    songs_id = re.findall(r'"song.*?id":(\d+)', res)
    return list(set(songs_id))

  def get_comments(self, ids):
    offset, total = 0, 0
    while True:
      # 通过offset来控制翻页，每页增加20， total除第一页是true外，其他页均为false
      text = '{rid: "", offset: "'+str(offset)+'", total: "'+('false' if offset > 0 else 'true')+'", limit: "100", csrf_token: ""}'
      url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_'+ids+'?csrf_token='

      params = {
        'params': str(self.get_params(self.key, text), 'utf-8'),
        'encSecKey': self.encSecKey
      }
      res = requests.post(url, headers=self.headers, data=params).text
      
      userId = re.findall(r'"userId":(\d+)', res)

      # 判断当前页是否有该用户的评论
      if self.uid in userId:
        content = re.search('userId":'+self.uid+'.*?beReplied.*?].*?content":"(.*?)"', res).group(1)
        comments = {
          "song": "https://music.163.com/#/song?id=" + ids,
          "page": '评论在：' + str(int((offset+100)/20-4)) + '-' + str(int((offset+100))/20) + '页',
          "content": content
        }
        self.comments.append(comments)
        print(comments)
        break

      # 取出总页数
      if offset == 0:
        total = int(re.search(r'"total":(\d+)', res).group(1))
      
      offset += 100

      if offset > total:
        break
        
  def get_params(self, key, text):
    h_enctext = self.aes_encrpt(key, text)
    # 其中‘biaobiaobiaobiao’是和上面的encSecKey是配套的，要改两部分都需要改，必须使用同一个16位随机字符串才可以。
    h_enctext = self.aes_encrpt('biaobiaobiaobiao', str(h_enctext, 'utf-8'))
    return h_enctext
   
  def aes_encrpt(self, key, text):
    iv = '0102030405060708'
    pad = 16 - len(text) % 16  # 加密长度要达到16位
    text +=  pad * chr(pad)    # 不够的在后面补充占位符
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = encryptor.encrypt(text.encode('utf-8'))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

if __name__ == '__main__':
    uid = input('请输入用户的id:')  # '127549532'
    netease = Netease(uid)
    pool = Pool(5)
    songs = netease.getTopMusic()
    print(songs)
    song = [x for x in songs]
    pool.map(netease.get_comments, song)
    pool.close()
    pool.join()
    