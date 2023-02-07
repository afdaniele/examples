import random
import time

from pynng import Pair0

port = "5556"
stats_every_secs = 5
buffer = 2048


if __name__ == '__main__':
    address = f"tcp://*:{port}"
    pair = Pair0(listen=address)

    i = 0
    last_time = time.time()
    data = bytes(random.getrandbits(8) for _ in range(buffer))
    print("PAIR (server) node started...")
    while True:
        pair.send(data)
        i += 1
        time.sleep(1)
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int((i * buffer) / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}secs is {speed}B/s")
