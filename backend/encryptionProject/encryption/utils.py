import secrets
from Crypto.Cipher import DES3 
from Crypto.Random import get_random_bytes 
from Crypto.Cipher import AES 
import hashlib
import os
import base64


def expand_key(key, length):
    """Expand the user's key to a fixed-length secure key using SHA-256."""
    return hashlib.sha256(key.encode()).digest()[:length]
# one-time pad encryption / decryption

def otp_encrypt(plain_text,key):
    if len(key) != len(plain_text):
        raise ValueError("Key length must much the length of the pliantext.")
    key_bytes = key.encode('utf-8')
    plain_bytes = plain_text.encode('utf-8')
    encrypted =bytes([plain_bytes[i] ^ key_bytes[i] for i in range(len(plain_text))])
    return encrypted.hex(),key

def otp_decrypt(encrypted_text,key):
    try:
        encrypted_bytes = bytes.fromhex(encrypted_text)
        key_bytes = key.encode('utf-8')
        if len(key_bytes) != len(encrypted_bytes):
            raise ValueError("Key length must match the length of the encrypted text.")
        decrypted = bytes([encrypted_bytes[i] ^ key_bytes[i] for i in range(len(encrypted_bytes))])

        return decrypted.decode('utf-8')
    except Exception:
        raise ValueError("Invalid key or encrypted text")


# Triple DES (3DES) Encryption

def pad(text,block_size=16):
    padding_length = block_size - (len(text) % block_size)
    return text + chr(padding_length) * padding_length

def unpad(text):
    return text[:-ord(text[-1])]

def des3_encr(plain_text,key):
    key = expand_key(key,24)
    key = key[:24]
    iv = os.urandom(8)
    cipher = DES3.new(key,DES3.MODE_CBC,iv)
    encrypted = cipher.encrypt(pad(plain_text,8).encode('utf-8'))
    return base64.b64encode(iv + encrypted).decode(),key.hex()

def des3_decrypt(encrypted_text,key):
    try:
        key = expand_key(key,24)
        key = key[:24]
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:8]
        cipher = DES3.new(key,DES3.MODE_CBC,iv)
        decrypted = cipher.decrypt(encrypted_data[8:]).decode('utf-8')
        return unpad(decrypted)
    except Exception:
        raise ValueError("Invalid key or encrypted text")

# AES Encryption and Decryption

def aes_encrypt(plain_tex,key):
    key = expand_key(key,32)
    key = key[:32]
    iv = os.urandom(16)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    padded_text = pad(plain_tex,16).encode('utf-8')
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(iv+encrypted).decode(),key.hex()

def aes_decrypt(encrypted_text,key):
    try:
        key = expand_key(key,32)
        key = key[:32]
        encrypted_data = base64.b64decode(encrypted_text)
        iv = encrypted_data[:16]
        cipher = AES.new(key,AES.MODE_CBC,iv)
        decrypted = cipher.decrypt(encrypted_data[16:]).decode('utf-8')
        return unpad(decrypted)
    except Exception:
        raise ValueError("Invalid key or encrypted text")

