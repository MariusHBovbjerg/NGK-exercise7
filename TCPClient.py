import sys
import socket
from lib import Lib


serverAddrPort = ("10.0.0.1",9000)
BUFSIZE = 1024

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("Write 'u' for uptime or 'l' for load average")
        msg = input()
        print("Sending message")
        bytesToSend = str.encode(msg)
        s.sendto(bytesToSend,serverAddrPort)
        data, addr = s.recvfrom(BUFSIZE)
        print("connection from: {}".format(addr))
        print(data.decode())

if __name__ == "__main__":
   main(sys.argv[1:])
