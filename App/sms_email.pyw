"""Send sms when pc is ON when connected to internet"""
import requests
import subprocess
import smtplib
from email.message import EmailMessage


class Message:
    def __init__(self):
        """BELOW are sms details"""
        self.message = '[SYSTEM IS ON!!]' + '\n' + subprocess.run('systeminfo', text=True, shell=True, capture_output=True).stdout.split('Domain:')[0]
        self.phone_numbers = '8837833685'
        self.api_key = 'IXjnZCuSsB9UOtaD0b2wP1xR3VNkq6vd4HGyLfQzWTFm85cMlp3ikshcfUVt0BzYxbWe1rESMlpyTFIv'
        self.url = "https://www.fast2sms.com/dev/bulk"
        self.payload = f"sender_id=FSTSMS&message={self.message}&language=english&route=p&numbers={self.phone_numbers}"
        self.headers = {'authorization': self.api_key, 'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache"}

        """BELOW are email details"""
        self.sender_email = 'anonymous.second.anonymous@gmail.com'
        self.password = 'P_assword'

        self.receiver_email = 'anonymous.second.anonymous@gmail.com'

        self.em = EmailMessage()
        self.em['Subject'] = 'MAKE SERVER ON!!'
        self.em['From'] = self.sender_email
        self.em['To'] = self.receiver_email
        self.em.set_content(self.message)

    def send_sms(self):
        try:
            while True:
                if Message.is_connected():
                    requests.request("POST", self.url, data=self.payload, headers=self.headers)
                    break
                else:
                    continue
        except Exception as msg:
            print(msg)

    def send_email(self):
        try:
            while True:
                if Message.is_connected():
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
                        conn.login(self.sender_email, self.password)
                        conn.send_message(self.em)  # Here we use send_message meathod
                    break
                else:
                    continue
        except Exception as msg:
            print(msg)

    @classmethod
    def is_connected(cls):
        try:
            requests.get('https://www.google.com/')
            return True
        except requests.exceptions.ConnectionError as msg:
            return False


obj = Message()
obj.send_sms()
obj.send_email()
