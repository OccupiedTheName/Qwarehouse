__author__ = 'XMKZ'
from socket import *
import thread
import os
import ctypes
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12


FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.

BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.



class Color:
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def set_cmd_color(self, color, handle=std_out_handle):
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool

    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)

    def print_red_text(self, print_text):
        self.set_cmd_color(4 | 8)
        print print_text
        self.reset_color()


    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        c = raw_input(print_text)
        self.reset_color()
        return c


    def print_yellow_text(self, print_text):
        self.set_cmd_color(6 | 8)
        print print_text
        self.reset_color()


    def print_blue_text(self, print_text):
        self.set_cmd_color(1 | 10)
        print print_text
        self.reset_color()

clr = Color()
'''
clr.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
clr.print_red_text('red')
clr.print_green_text(" ")
clr.print_blue_text('blue')
clr.print_yellow_text('yellow')
'''

HOST = '127.1.0.0'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)



# Login

clr.print_green_text('welcome to JL Mark 1.01')
clr.print_green_text('This new Mark 1.0.1 which add a login system')

while 1:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    print 'name?(Ed/Big_Dk_Pan/James/Purple)'
    name=raw_input('> ')
    tcpCliSock.send(name)
    print 'password?'
    pswd=raw_input('> ')
    tcpCliSock.send(pswd)
    ans=tcpCliSock.recv(BUFSIZ)
    if ans=='Y':
        print 'welcome, '+name
        break
    else:
        print 'try again kid, can you hack in?(okay...i guess it is easy to hack in)'
        print 'type your name again'

#encode

#decode

#Chatting room
def recv():
    while 1:
        data1 = tcpCliSock.recv(BUFSIZ)
        if not data1:
            break
        clr.print_green_text(data1)

def snd():
    while 1:
        data = raw_input('> ')
        if data == 'exit':
            exit(0)
            break
        if not data:
            continue
        tcpCliSock.send(data)
try:
    thread.start_new_thread(recv, ())
    thread.start_new_thread(snd, ())
except:
    print "Error"
while 1:
    pass
tcpCliSock.close()