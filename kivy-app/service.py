import time
import asyncio
import websockets

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% python service activate')

async def response(websocket, path):
    msg = await websocket.recv()
    print("msg:", msg)
    await websocket.send("ok from local")


def start_server():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ staarting python server")
    server = websockets.serve(response, '127.0.0.1', 8077)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
    print("$$$$$$$$$$$$$$$$ finish python server")

start_server()
print ('service started')
asyncio.sleep(100)
print ('---service ended')
