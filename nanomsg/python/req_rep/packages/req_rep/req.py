import time

from pynng import Req0

port = "5556"
stats_every_secs = 5


if __name__ == '__main__':
    address = f"tcp://rep:{port}"
    req = Req0(dial=address)

    i = 0
    request = b"payload"
    last_time = time.time()
    print("REQ node started...")
    while True:
        req.send(request)
        response = req.recv()

        assert response == request
        i += 1
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int(i / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}s is {speed} r/s")
