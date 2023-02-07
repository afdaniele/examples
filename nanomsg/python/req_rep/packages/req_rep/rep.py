import time

from pynng import Rep0

port = "5556"
stats_every_secs = 5


if __name__ == '__main__':
    address = f"tcp://*:{port}"
    rep = Rep0(listen=address)

    i = 0
    last_time = time.time()
    print("REP node started...")
    while True:
        request = rep.recv()
        rep.send(request)

        i += 1
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int(i / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}s is {speed} r/s")
