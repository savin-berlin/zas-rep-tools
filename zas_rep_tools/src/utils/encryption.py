#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# : Encryptor
# Author:
# c(Student) ->     {'Egor Savin'}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###Programm Info######

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
#import pkcs7
import StringIO
import binascii


class Encryptor:

    def __init__(self):
        pass

    def Encrypt(self, PlainText, SecurePassword):
        pw_encode = SecurePassword.encode('utf-8')
        text_encode = PlainText.encode('utf-8')

        key = hashlib.sha256(pw_encode).digest()
        iv = Random.new().read(AES.block_size)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        pad_text = encode(text_encode)
        msg = iv + cipher.encrypt(pad_text)

        EncodeMsg = base64.b64encode(msg)
        return EncodeMsg

    def Decrypt(self, Encrypted, SecurePassword):
        decodbase64 = base64.b64decode(Encrypted.decode("utf-8"))
        pw_encode = SecurePassword.decode('utf-8')

        iv = decodbase64[:AES.block_size]
        key = hashlib.sha256(pw_encode).digest()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        msg = cipher.decrypt(decodbase64[AES.block_size:])
        pad_text = decode(msg)

        decryptedString = pad_text.decode('utf-8')
        return decryptedString

    



    def decode(text, k=16):
        nl = len(text)
        val = int(binascii.hexlify(text[-1]), 16)
        if val > k:
            raise ValueError('Input is not padded or padding is corrupt')

        l = nl - val
        return text[:l]


    def encode(text, k=16):
        l = len(text)
        output = StringIO.StringIO()
        val = k - (l % k)
        for _ in xrange(val):
            output.write('%02x' % val)
        return text + binascii.unhexlify(output.getvalue())




import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

