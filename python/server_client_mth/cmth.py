import socket as sck 
from threading import Thread, Lock
mutex = Lock()

server = ("127.0.0.1", 8000)


class Rec(Thread):
    def __init__(self, con):
        Thread.__init__(self)
        self.con = con

    def run(self):
        while True:
         mutex.acquire()

         message = self.con.recv(4096)
         #sensore 1;sensore 2 (sono boleani)
         print(message.decode())
         mutex.release()


def main():
    soc = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    soc.connect(server)

    rec_thread = Rec(soc)
    rec_thread.start()

    while True:
        mex = input("mex: ")
        message = f"{mex}".encode()
        soc.sendall(message)
        if mex.lower() == "exit":
            break

    soc.close()


if __name__ == "__main__":
    main()