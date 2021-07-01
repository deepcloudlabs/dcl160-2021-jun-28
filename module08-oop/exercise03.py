import asyncio
import json

import websockets

"""
{'e': 'trade', 'E': 1625129672319, 
's': 'BTCUSDT', 't': 940985816, 'p': '33407.37000000', 'q': '0.00053400', 
'b': 6701262151, 'a': 6701262192, 'T': 1625129672318, 'm': True, 'M': True}
"""

trading_data = {
}

trades = []


async def consumer_handler(frames):
    global trading_data
    global trades
    async for frame in frames:
        trade = json.loads(frame)
        trades.append(trade)
        # print(trade)
        if len(trades) % 10_000 == 0:
            my_trades = trades[:]
            for tr in my_trades:
                bid_id = tr['b']
                ask_id = tr['a']
                volume = float(tr['p']) * float(tr['q'])
                if bid_id in trading_data:
                    trading_data[bid_id]["buy"] += volume
                    trading_data[bid_id]["count"] += 1
                else:
                    trading_data[bid_id] = {
                        "sell": 0
                    }
                    trading_data[bid_id]["buy"] = volume
                    trading_data[bid_id]["count"] = 1
                if ask_id in trading_data:
                    trading_data[ask_id]["sell"] += volume
                    trading_data[ask_id]["count"] += 1
                else:
                    trading_data[ask_id] = {
                        "buy": 0
                    }
                    trading_data[ask_id]["sell"] = volume
                    trading_data[ask_id]["count"] = 1
            trading_data = {id: volume for id, volume in
                            sorted(trading_data.items(), key=lambda item: item[1]["count"], reverse=True)}
            print(trading_data)


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()
