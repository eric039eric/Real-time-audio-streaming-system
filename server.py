import asyncio, websockets, sounddevice as sd, numpy as np

SAMPLE_RATE = 16_000
BLOCK      = 1024          # 每次錄 1024 個 sample，比較穩定

clients = set()
q       = asyncio.Queue()

def audio_callback(indata, frames, time, status):
    loop.call_soon_threadsafe(q.put_nowait, indata.tobytes())

async def audio_stream(ws):
    clients.add(ws)
    try:
        while True:
            await asyncio.sleep(1)
    finally:
        clients.discard(ws)

async def pump():
    with sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16',        # 確保 16-bit
            blocksize=BLOCK,
            callback=audio_callback):
        while True:
            data = await q.get()
            for ws in clients.copy():
                try:
                    await ws.send(data)
                except websockets.ConnectionClosed:
                    clients.discard(ws)

async def main():
    global loop
    loop = asyncio.get_running_loop()
    await websockets.serve(audio_stream, '0.0.0.0', 5678)
    print("WS 伺服器 ws://localhost:5678 (16 kHz / int16 / 1-ch)")
    asyncio.create_task(pump())
    await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
