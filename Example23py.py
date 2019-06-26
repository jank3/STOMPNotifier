# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:47:41 2019

@author: janto
"""
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 9001))
asyncio.get_event_loop().run_forever()