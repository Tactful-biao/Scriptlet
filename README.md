# Scriptlet

用来写一些解决生活中小事情的脚本。
> 脚本中有不懂的地方，或者有问题的地方可以关注我的公众号： <b>一个简单程序猿</b> 获取帮助！

## 毛概模拟练习脚本

详情请到我的博客，上面有详细的介绍[毛概模拟练习](https://bbiao.me/2018/03/13/%E6%AF%9B%E6%A6%82%E6%A8%A1%E6%8B%9F%E7%BB%83%E4%B9%A0%E8%84%9A%E6%9C%AC/)

## script 目录
> 该目录下放一些平常会使用到的脚本。

+ get_ssr.py
  - 脚本介绍：get_ssr.py 是一个获取ssr链接的脚本。通过注册邮箱，获取一个临时邮箱，使用这个临时邮箱去注册，然后获取ssr。每次注册都可以获得3G流量的三天使用权限，用完可以继续注册。
  - 使用方法: python3 get_ssr.py
  - 运行效果：程序运行之后会自动申请邮箱，自动注册。然后自动提取ssr内容，提取的包括json文件和ssr链接。根据个人情况使用。
  - 用途： 科学上网

+ ssr_link_decode.py
  - 脚本介绍：ssr_link_decode.py是一个把ssr链接转换成对应的json内容的脚本
  - 使用方法：python3 ssr_link_decode.py
  - 运行效果： 输入ssr链接后面的内容，就会在当前目录下生成一个shadow.json文件，里面是对应的解码内容。
  - 用途：转换ssr链接到json文件，方便一些命令行使用。 
  - 项目地址见: [shadowsocksr](https://github.com/ssrbackup/shadowsocksr)通过修改里面的config.json来配置内容，但是很多时候别人分享的都是连接到形式，所以我们使用脚本自动把链接转换成对应的json内容，然后保存到本地，方便使用。

+ music.py
  - 脚本介绍： music.py是一个根据网易云音乐用户id获取他网易云评论的脚本（不是完全获取，只是根据他最喜欢听的100首歌曲里去找）。
  - 使用方法： python3 music.py , 然后输入用户的id。
  - 运行效果： 自动查找该用户在网易云音乐歌曲内的评论内容并打印出来， 可能时间比较久(该脚本需要优化)！
  - 用途：可以获得指定人的网易云评论内容。

+ music_list.py
  - 脚本介绍：该脚本是批量下载网易云歌单的一个脚本。
  - 运行方式： python3 music_list.py ， 然后输入歌单id。
  - 运行效果：会自动在当前目录创建一个music目录并把该歌单的所以可以下载的音乐下载到该目录下。
  - 用途：批量下载网易云音乐。

+ iphone12.py
  - 脚本介绍: 该脚本是之前提醒iPhone12是否有货的一个脚本。
  - 使用方法: python3 iphone12.py
  - 运行效果: 每10s去苹果官网查询一下我关注的某配置下的ipone12 是否有货，如果有货就给我发邮件。
  - 用途: 第一时间获取iphone的库存动态

+ book.index
  - 一个获取电子书的前端网页
  -- 讲解: [地址](https://zhuanlan.zhihu.com/p/381025985)
  - 详见: [地址](https//github.com/Simper-coder/js/tree/gh-pages/book)