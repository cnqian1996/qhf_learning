import requests
import gevent
from gevent import monkey
import urllib.request

monkey.patch_all()


def download(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    print('下载了{}的数据，长度：{}'.format(url, len(content)))


if __name__ == '__main__':
    urls = ['https://www.yunfanocean.com', 'http://www.baidu.com', 'http://www.163.com']
    g1 = gevent.spawn(download, urls[0])
    g2 = gevent.spawn(download, urls[1])
    g3 = gevent.spawn(download, urls[2])

    # gevent.joinall(g1, g2, g3)  # 类似 g1.join()
    g1.join()
    g2.join()
    g3.join()
