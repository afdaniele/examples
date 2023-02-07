import time

from pynng import Pair0

port = "5556"
stats_every_secs = 5


if __name__ == '__main__':
    buffer = None
    address = f"tcp://peer:{port}"

    pair = Pair0(dial=address)

    i = 0
    last_time = time.time()
    print("PAIR (client) node started...")
    while True:
        data = pair.recv()
        i += 1
        if buffer is None:
            buffer = len(data)
            print(f"Received first message, detected buffer of {buffer}B")
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int((i * buffer) / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}secs is {speed}B/s")
