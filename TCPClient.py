import sys
import socket
from lib import Lib


serverAddrPort = ("10.0.0.1",9000)
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("Write 'u' for uptime or 'l' for load average")
        msg = input()
        print("Sending message")
        s.sendto(msg.encode(),serverAddrPort)

if __name__ == "__main__":
   main(sys.argv[1:])
