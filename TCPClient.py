import sys
import socket
from lib import Lib


HOST = "10.0.0.1"
PORT = 9000
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connection established.")
        dir = "/home/ase/Desktop/NGK-exercise6/"
        dir = dir+argv[0]
        s.sendall((dir+"\0").encode())
        length = Lib.readTextTCP(s)
        print("Length of file is:", length,"bytes.")
        if(int(length)):
            print("Receiving file.")
            receiveFile(dir,s)
        else:
            print("File did not exist or was empty.")
        s.close()
        print("Connection closed")
    
def receiveFile(fileName,  conn):
    file = open(fileName,"w")
    print("Writing file.")
    file.write(Lib.readTextTCP(conn))
    file.close()
    print("File closed.")

if __name__ == "__main__":
   main(sys.argv[1:])
