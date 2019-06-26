# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:29:27 2019

@author: janto
"""

import asyncio
import websockets
import nest_asyncio


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8004)

nest_asyncio.apply()

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()