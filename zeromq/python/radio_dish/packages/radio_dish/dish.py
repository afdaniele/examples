import time
import zmq


protocol = "udp"
host = "*"
port = "5556"
group = "test"
stats_every_secs = 5


if __name__ == '__main__':
    buffer = None

    context = zmq.Context()
    socket = context.socket(zmq.DISH)

    # set a timeout for the blocking behavior
    # socket.rcvtimeo = 1000

    # DISH must bind: http://api.zeromq.org/master:zmq-udp
    socket.bind(f"{protocol}://{host}:{port}")
    socket.join(group)

    i = 0
    last_time = time.time()
    print("DISH node started...")
    while True:
        try:
            data = socket.recv(copy=False)
        except zmq.Again:
            # NOTE: this is only thrown in case of recv timeout as per `socket.rcvtimeo` above
            print('missed a message')
            continue
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
