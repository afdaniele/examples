import zmq
import random
import time


protocol = "udp"
host = "dish"
port = "5556"
group = "test"
stats_every_secs = 5


if __name__ == '__main__':
    context = zmq.Context()

    # RADIO must connect: http://api.zeromq.org/master:zmq-udp
    socket = context.socket(zmq.RADIO)
    socket.connect(f"{protocol}://{host}:{port}")

    buffer = 2048

    i = 0
    last_time = time.time()
    data = bytearray(random.getrandbits(8) for _ in range(buffer))
    print("RADIO node started...")
    while True:
        socket.send(data, group=group)
        i += 1
        time.sleep(1)
        # ---
        elapsed = time.time() - last_time
        if elapsed > stats_every_secs:
            last_time = time.time()
            speed = int((i * buffer) / elapsed)
            i = 0
            print(f"Average speed during last {stats_every_secs}secs is {speed}B/s")
