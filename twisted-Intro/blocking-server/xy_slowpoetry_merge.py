# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

"""
源程序改进：
main()中进行args的读取和socket的初始化，调用serve()完成工作
一、把两层while的外层while做成serve()函数
    函数功能：
    1 判断接入并获取接入信息tcpSocket.accept()
    2 调用send_poetry()函数发送数据
二、把内层函数抽象成发送诗歌信息的函数send_poetry()

"""
from socket import *
import time


def serve(tcpSocket):
    while True:
        print('waiting for connection')
        tcpClisock, addr = tcpSocket.accept()
        print('... connected from:', addr)
        send_poetry(tcpClisock)


def send_poetry(tcpClisock):
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


if __name__ == "__main__":
    HOST = ''
    PORT = 22000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpSocket = socket(AF_INET, SOCK_STREAM)
    tcpSocket.bind(ADDR)
    tcpSocket.listen(5)

    serve(tcpSocket)
