import re
import os
import requests


def tuPian(word):
    # 把关键字和我们的url拼接起来
    start_url = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + word + "&pn={}&ct=&ic=0&lm=-1&width=0&height=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    for i in range(10):  # 写一个循环, 可以得到更多的图片
        url = start_url.format(i * 60)  # 得到不同的url
        """获取当前页面所有图片的ulr列表"""
        r = requests.get(url, headers=headers)
        ret = r.text  # 得到源代码, 里面有每一张图片的url
        pic_url_list = re.findall('"objURL":"(.*?)",.*?""', ret)  # 找到所有图片的url, 提取出来
        print('*' * 50)
        print('-----正在保存第%d页图片-----' % (i + 1))
        for pic_url in pic_url_list:
            print(pic_url)

            # 有的名字里面有/, 不能允许, 所以得替换成空, 并且图片名字以url后10位来命名
            path = re.sub('/', '', pic_url[-10:])

            # 判断url是不是以图片类型来结尾
            end = re.search('(\.jpg|\.jpeg|\.png)$', path)
            if end == None:
                # 如果不是以图片类型来结尾, 就加上一个后缀名
                path = path + '.png'

            # 因为有的图片url已经失效了, 所以访问肯定会失败, 我们就得捕获异常
            try:
                # 保存的路径和图片名字的拼接
                with open('./' + word + '/{}'.format(path), 'ab') as f:
                    pic = requests.get(pic_url, headers=headers, timeout=1)
                    f.write(pic.content)
                    print('正在下载第%d张图片' % (pic_url_list.index(pic_url) + 1))
            except Exception:
                pass


if __name__ == '__main__':
    word = input('请输入关键字: ')
    if not os.path.exists(word):
        os.mkdir(word)  # 创建文件夹
    tuPian(word)
