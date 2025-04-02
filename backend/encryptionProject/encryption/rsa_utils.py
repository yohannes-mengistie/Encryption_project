from Crypto.PublicKey import RSA

'''RSA by it self it is deterministic which means the same text or message will have the same encryption 
any time  when try to  encrypt. to solve this I use PKCS1_OAEP which is a padding scheme for RSA.
 '''
from Crypto.Cipher import PKCS1_OAEP  
import base64

# It just Load RSA keys from files
def load_keys():
    with open(r"C:\Users\Lenovo\OneDrive\Desktop\Symmetric_Encryption_Project\backend\private_key.pem", "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())
    with open(r"C:\Users\Lenovo\OneDrive\Desktop\Symmetric_Encryption_Project\backend\public_key.pem", "rb") as pub_file:
        public_key = RSA.import_key(pub_file.read())
    return private_key, public_key

# Encrypt message using the public key
def rsa_encrypt(message):
    _, public_key = load_keys()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

# Decrypt message using the private key
def rsa_decrypt(encrypted_message):
    private_key, _ = load_keys()
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()
