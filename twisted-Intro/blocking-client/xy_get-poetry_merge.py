# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

"""
TCP 客户端
修改用于接收block-poetry-server

改动：
    1 处理用户输入
        1.1 可接受多组IP和端口输入
        1.2 可适应两种IP及端口号的输入形式： "127.0.0.1 99" / "127.0.0.1:99"
    2 新建poet变量
        使poet+=data，在每次循环之后刷新poet显示，这样就能达到慢慢输出成为一整篇文章的效果
    3 format_address()
        将用户输入整理成socket.connect()格式
TODO:
    1 优雅退出：
        把while循环放到try-catch中，捕获EOF error和Keyinterrupt error，在except写close()
    2 调整BUFFSIZE（目前为1024）
"""

from socket import *
import optparse


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

            This is the Get Poetry Now! client, blocking edition.
            Run it like this:

              python get-poetry.py port1 port2 port3 ...

            If you are in the base directory of the twisted-intro package,
            you could run it like this:

              python blocking-client/get-poetry.py 10001 10002 10003

            to grab poetry from servers on ports 10001, 10002, and 10003.

            Of course, there need to be servers listening on those ports
            for that to work.
            """

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


def client(tcpCliSock):
    poem = ''
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        poem += data

    tcpCliSock.close()


if __name__ == '__main__':
    HOST = 'localhost'
    print("connecting to localhost...")
    PORT = int(raw_input("port > "))
    # BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    client(tcpCliSock)
