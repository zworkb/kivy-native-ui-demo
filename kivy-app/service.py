import time
import asyncio
import websockets

async def response(websocket, path):
    msg = await websocket.recv()
    print("msg:", msg)
    await websocket.send("echo: %s" % msg)


def start_server():
    server = websockets.serve(response, '127.0.0.1', 8077)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()

start_server()
asyncio.sleep(100)
print ('---service ended')
