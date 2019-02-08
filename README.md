# Scriptlet

用来写一些解决生活中小事情的脚本。

## 毛概模拟练习脚本

详情请到我的博客，上面有详细的介绍[毛概模拟练习](https://bbiao.me/2018/03/13/%E6%AF%9B%E6%A6%82%E6%A8%A1%E6%8B%9F%E7%BB%83%E4%B9%A0%E8%84%9A%E6%9C%AC/)

## script 目录

该目录下放一些平常会使用到的脚本。

### ssr_link_decode 是一个把ssr链接转换成对应的json内容的脚本

## 使用方法

> python3 ssr_link_decode

输入ssr链接后面的内容，就会在当前目录下生成一个shadow.json文件，里面是对应的解码内容。

## 用途

> 现在ssr越来越普遍，而ssr的客户端却不是很普遍(Linux下)，通过查找替代方案，通过配置使用终端进行连接。
项目地址见: [shadowsocksr](https://github.com/ssrbackup/shadowsocksr)

通过修改里面的config.json来配置内容，但是很多时候别人分享的都是连接到形式，所以我们使用脚本自动把链接转换成对应的json内容，然后保存到本地，方便使用。
