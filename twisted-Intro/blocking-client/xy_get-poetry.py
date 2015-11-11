# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

"""
TCP 客户端
修改用于接收block-poetry-server


TODO:
    优雅退出：
        把while循环放到try-catch中，捕获EOF error和Keyinterrupt error，在except写close()
    调整BUFFSIZE
"""

from socket import *


def client(tcpCliSock):
    while True:
        data = tcpCliSock.recv(1024)
        if not data:
            break
        print(data)

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
