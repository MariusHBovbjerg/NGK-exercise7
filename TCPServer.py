import sys
import socket
from lib import Lib

HOST = ""
PORT = 9000
BUFSIZE = 1024

def checkClientInput(x):
    return {
        'l': 1,
        'L': 1,
        'u': 2,
        'U': 2
    }.get(x, 0)

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print("Server is listening.")
        while True:
            data, addr = s.recvfrom(BUFSIZE)

            print("connection from: {}".format(addr))
            request = checkClientInput(data.decode())

            if request == 1:

                print("l or L was received")
                sendFile("/proc/loadavg",s,addr)
                
            elif request == 2:
                
                print("u or U was received")
                sendFile("/proc/uptime",s,addr)

            else:
                print("Neither was received")
                s.sendto(b"Yo, wrong code buddy",addr)


def sendFile(fileName, conn,addr):
    file = open(fileName,"r")
    TEXTBUF = file.read(BUFSIZE)
    print("Read:",len(TEXTBUF), ".")
    while(TEXTBUF):
        #Lib.writeTextTCP(TEXTBUF,conn)
        conn.sendto(TEXTBUF.encode(),addr)
        TEXTBUF = file.read(BUFSIZE)
        print("Read:",len(TEXTBUF),".")
    file.close
    print("File closed.")

if __name__ == "__main__":
   main(sys.argv[1:])
