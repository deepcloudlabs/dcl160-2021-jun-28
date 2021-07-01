import asyncio
import json

import websockets

"""
{'e': 'trade', 'E': 1625129672319, 
's': 'BTCUSDT', 't': 940985816, 'p': '33407.37000000', 'q': '0.00053400', 
'b': 6701262151, 'a': 6701262192, 'T': 1625129672318, 'm': True, 'M': True}
"""


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        print(trade)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()
