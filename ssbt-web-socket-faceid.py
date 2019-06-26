# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:52:19 2019

@author: janto
"""

from simple_websocket_server import WebSocketServer, WebSocket


class ssbt_socket_face_id(WebSocket):
    def handle(self):
        # echo message back to client
        self.send_message(self.data)
    
    def connected(self):
        print(self.address, 'connected')
    
    def handle_close(self):
        print(self.address, 'closed')


server = WebSocketServer('127.0.0.1', 61613, ssbt_socket_face_id)
server.serve_forever()