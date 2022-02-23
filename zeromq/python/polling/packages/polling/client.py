from collections import defaultdict

import time
import zmq


port = 5557
stats_every_secs = 5


if __name__ == '__main__':
    buffer = None

    context = zmq.Context()

    # socket 0
    socket0 = context.socket(zmq.PAIR)
    socket0.connect(f"tcp://peer:{port}")

    # socket 1
    socket1 = context.socket(zmq.PAIR)
    socket1.connect(f"tcp://peer:{port + 1}")

    poller = zmq.Poller()
    poller.register(socket0, zmq.POLLIN)
    poller.register(socket1, zmq.POLLIN)

    i = 0
    peers = defaultdict(lambda: 0)
    last_time = time.time()
    print("POLLER (client) node started...")
    while True:
        events = dict(poller.poll())

        for socket, event in events.items():
            if event != zmq.POLLIN:
                continue

            data = socket.recv()
            peer = data.decode("ascii")
            peers[peer] += 1

            i += 1
            elapsed = time.time() - last_time
            if elapsed > stats_every_secs:
                last_time = time.time()
                speed = int(i / elapsed)
                i = 0
                print(dict(peers))
                print(f"Average speed during last {stats_every_secs}secs is {speed}msg/s")
