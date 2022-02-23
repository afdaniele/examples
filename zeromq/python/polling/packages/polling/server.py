from threading import Thread

import zmq
import time


port = 5557
stats_every_secs = 5

context = zmq.Context()


def server(k: int):
    socket = context.socket(zmq.PAIR)
    socket.bind(f"tcp://*:{port + k}")
    i = 0
    last_time = time.time()
    print(f"PEER{k}: (server) node started...")
    while True:
        socket.send(f"{k}".encode("ascii"))
        i += 1
        time.sleep(0.001)
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int(i / elapsed)
            i = 0
            print(f"PEER{k}: Average speed during last {stats_every_secs}secs is {speed}msg/s")


if __name__ == '__main__':
    server0 = Thread(target=server, args=(0,), daemon=True)
    server1 = Thread(target=server, args=(1,), daemon=True)
    server0.start()
    server1.start()
    # wait for servers to terminate
    server0.join()
    server1.join()
