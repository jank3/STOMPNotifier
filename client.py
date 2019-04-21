# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:34:22 2019

@author: janto
"""

import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = 'http://localhost/ssbt-websocket' 
port = 8080 

try: 
    s.bind((host, port)) 
except socket.error as e: 
    print(str(e)) 
    s.connect((host, port)) 
    print(s.recv(1024)) 
    s.close() 