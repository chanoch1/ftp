import socket          # client

PORT = 1337 # The port used by the server

def conect_to_socket(f):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.send(f)
#       print('Received',repr(data))

def send_file():
        with open('/home/chvidis/ch/students.ods', 'rb') as f:
                while True:
                        data = f.read(4096)
                        if len(data) == 0:
                                break
                        conect_to_socket(data)

def Get_a_file_and_download():
        data = conn.recv(4096)
        pass

if __name__=="__main__":
        print('enter the requred ip')
        HOST = input()
        send_file()
#       Get_a_file_and_download(
