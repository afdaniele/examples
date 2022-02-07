import zmq
import random
import time


port = "5556"
stats_every_secs = 5


if __name__ == '__main__':
    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://rep:%s" % port)

    i = 0
    request = b"payload"
    last_time = time.time()
    print("REQ node started...")
    while True:
        socket.send(request)
        response = socket.recv()
        assert response == request
        i += 1
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int(i / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}s is {speed} r/s")
