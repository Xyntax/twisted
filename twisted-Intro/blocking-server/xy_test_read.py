# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'
import os
import time


"""
证明了file.read()自动推进
以及socket.sendall()每次发送的确实10个字符
"""


inputf = open("../poetry/ecstasy.txt")
# bytes = inputf.read(int(raw_input("bytes per time > ")))

while True:
    bytes = inputf.read(10)
    if not bytes:  # no more poetry :(
        inputf.close()
        print("No more poetry! ")

    print 'Sending %d bytes' % len(bytes)

    try:
        print(bytes)  # this is a blocking call
    except:
        inputf.close()
        print "user end!"

    time.sleep(1)
