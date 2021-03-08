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
                
            data = s.recvfrom(BUFSIZE)
            datamsg = data[0]
            dataaddr = data[1]

            print("connection from: {}".format(dataaddr))

            request = checkClientInput(datamsg)

            if request == 1:

                print("l or L was received")
                
            elif request == 2:
                
                print("u or U was received")

            else:
                print("Neither was received")


def sendFile(fileName, conn):
    file = open(fileName,"r")
    TEXTBUF = file.read(BUFSIZE)
    print("Read:",len(TEXTBUF), ".")
    while(TEXTBUF):
        #Lib.writeTextTCP(TEXTBUF,conn)
        conn.send(TEXTBUF.encode())
        TEXTBUF = file.read(BUFSIZE)
        print("Read:",len(TEXTBUF),".")
    conn.send(b'\0')
    file.close
    print("File closed.")

if __name__ == "__main__":
   main(sys.argv[1:])
