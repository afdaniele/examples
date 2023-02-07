import random
import time

from pynng import Pub0


port = "5556"
stats_every_secs = 5


if __name__ == '__main__':
    address = f"tcp://*:{port}"
    pub = Pub0(listen=address)

    buffer = 2048

    i = 0
    last_time = time.time()
    data = bytes(random.getrandbits(8) for _ in range(buffer))
    print("PUB node started...")
    while True:
        pub.send(data)
        i += 1
        time.sleep(1)
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int((i * buffer) / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}secs is {speed}B/s")
