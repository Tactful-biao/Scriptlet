import requests
import re
import os
from bs4 import BeautifulSoup
from multiprocessing.pool import Pool

# 歌曲保存目录 当前文件的music目录下
path = 'music'
headers = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
}


def get_music_id(mid='4892940786'):
    '''
    获取歌单内的所有歌曲id和歌曲名称
    :param mid: 歌单id
    :return: 歌曲的打包信息
    '''

    data = []
    url = 'https://music.163.com/playlist?id=' + mid
    res = requests.get(url, headers=headers).text

    # 获取歌单内的所有歌曲id
    song_id = re.findall('/song\?id=(\d+)', res)

    # 获取歌单内的歌曲名称
    soup = BeautifulSoup(res, 'lxml')
    song_name = [song.getText() for song in soup.find('ul', attrs={'class': 'f-hide'}).find_all('a')]

    # 对歌曲名称和id值进行打包处理
    for _id, _name in zip(song_id, song_name):
        data.append((_id, _name))

    return data


def download(info):
    '''
    把歌单能下载的音乐下载到music目录下，通过判断歌曲的大小来判断该歌曲是否可播放
    :param info: 歌曲的名称和id
    :return: None
    '''
    # 歌曲id
    mid = info[0]

    # 歌曲名称
    music_name = info[1]

    # 构造歌曲下载链接
    down_link = 'http://music.163.com/song/media/outer/url?id='+mid+'.mp3'

    # 下载歌曲
    if not os.path.exists(path + '/' + music_name + '.mp3'):
        with open(path + '/' + music_name+'.mp3', 'wb') as mp3:
            mp3.write(requests.get(down_link, headers=headers).content)
        print(music_name + ' 已经下载完成！')

    if os.path.getsize(path + '/' + music_name + '.mp3') < 102400:
        os.remove(path + '/' + music_name + '.mp3')


if __name__ == '__main__':
    if not os.path.exists(path):
        os.mkdir(path)
    pool = Pool(10)
    mid = input('请输入歌单id: ')
    music_info = [mid for mid in get_music_id(mid)]
    pool.map(download, music_info)
    pool.close()
    pool.join()
