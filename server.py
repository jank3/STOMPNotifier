# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:32:45 2019

@author: janto
"""

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '' 
port = 61613 
s.bind((host, port)) 
s.listen(5) 

while True: 
    c, addr = s.accept() 
    print('Got connection from', addr) 
    c.send(b'Thank you for connecting') 
    c.close() 