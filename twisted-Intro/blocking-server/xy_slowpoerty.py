# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

"""
测试结果

1.阻塞(block).

    这个TCP服务器程序运行时，先后使用两次nc localhost port连接。
    在第一首诗歌没有发送完成时，阻塞。直到data ends才开始第二个连接发送。

    waiting for connection
    ('... connected from:', ('127.0.0.1', 41354))
    data ends
    waiting for connection
    ('... connected from:', ('127.0.0.1', 41379))

2.对于客户端连接的检测.

    tcpClisock, addr = tcpSocket.accept()
    这个函数会自身循环，一直到有客户端接入，将两个结果return之后，才进行下一句。
    所以这个检测客户端接入的过程不需要程序员手动写。

3.TODO.

    程序ctrl-c之后无法自动回收端口
    客户端断开之后，socket.error: [Errno 32] Broken pipe
"""

from socket import *
import time

HOST = ''
PORT = 21000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
    print('waiting for connection')
    tcpClisock, addr = tcpSocket.accept()
    print('拿到数据了')
    print('... connected from:', addr)

    file = open("../poetry/ecstasy.txt")
    while True:
        data = file.read(20)
        if not data:
            print("data ends")
            tcpClisock.close()
            file.close()
            break
        tcpClisock.send(data)
        time.sleep(1)
