# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:34:22 2019

@author: janto
"""

import socket 
import stomp

url = "ws://localhost:8080/ssbt-websocket"
c = stomp.Connection([('localhost/ssbt-websocket', 8080)])
c.set_listener('', PrintingListener())
c.start()
c.connect('ssbt_1', 'Password1', wait=True)

c.subscribe('/queue/IDCamRecognized', 123)
c.send('/queue/IDCamRecognized', 'a test ID')
