import socket            # server

HOST = '127.0.0.1' #to connect with my pc
PORT = 1337 #casual port

# appropriate to IPv4 and protocol TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Assigns to specific interface and port
        s.bind((HOST,PORT))
        # The server continues to listen to the client
        s.listen()
        # Communicates with the client
        conn, addr = s.accept()
        with conn:
                print('Connected by', addr)
                while True:
                        data = conn.recv(1024)
                        if not data:
                                break
                        print(data)
                        conn.sendall(data)

