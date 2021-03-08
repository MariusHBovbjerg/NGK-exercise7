import sys
import socket
from lib import Lib

HOST = ""
PORT = 9000
BUFSIZE = 1000

def main(argv):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            while conn:
                print('Connected by', addr, ".")
                
                data = Lib.readTextTCP(conn)
                filesize = Lib.check_File_Exists(data)
                if (filesize):
                    filesizeStr = str(filesize) + "\0"
                    conn.send(filesizeStr.encode())
                    sendFile(data,conn)
                else:
                    filesizeStr = str(filesize) + "\0"
                    conn.send(filesizeStr.encode())
                conn.close()
                conn = None
                print("Connection closed")

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
