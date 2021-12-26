# encoding:utf-8
from Crypto.Cipher import AES
import base64

def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return (text)

def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(password, AES.MODE_ECB)
    data = cipher.encrypt(pad(data))
    return (data)
    
if __name__ == '__main__':
    data = 'ni hao'
    password = 'aesrsasec' #16,24,32位长的密码
    password = add_to_16(password)        
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print ('encrypt_data:', encrypt_data)