import base64
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import EncryptedMessage
from .utils import otp_decrypt,otp_encrypt,aes_decrypt,aes_encrypt,des3_decrypt,des3_encr,expand_key
from .rsa_utils import rsa_encrypt,rsa_decrypt,load_keys

def serialize_rsa_key(rsa_key):
    """Convert an RSA key to a PEM-encoded string for storage."""
    return base64.b64encode(rsa_key.export_key(format="PEM")).decode('utf-8')



@api_view(['POST'])
def encrypt_message(request):
    data = request.data
    message = data.get('message')
    key = data.get('key')
    _,public_key = load_keys()
    algorithm = data.get('algorithm')

    if not algorithm == 'RSA' and (not message or not key or not algorithm):
        return Response({'error': "Message,key,and algorithm are required"},status=400)
    
    else:
    
        if algorithm == 'OTP':
            if len(key) != len(message):
                    return Response({'error': 'Key length must match message length for OTP'}, status=400)
            encrypted,used_key = otp_encrypt(message,key)
        elif algorithm == 'DES3':
            encrypted,used_key = des3_encr(message,key)
        elif algorithm == 'AES':
            encrypted,used_key = aes_encrypt(message,key)
        elif algorithm == 'RSA':
            encrypted = rsa_encrypt(message)
            used_key = serialize_rsa_key(public_key)
        
        else:
            return Response({'error':'Invalid encryption algorithm'},status=400)
        
        encrypt_message = EncryptedMessage.objects.create(message=encrypted,key=used_key,algorithm=algorithm)
        return Response({'plain_text':message,'encrypted_message':encrypted,'key':used_key,'algorithm':algorithm})

@api_view(['POST'])
def decrypt_message(request):
    data = request.data
    encrypted_message = data.get('encrypted_message')
    key = data.get('key')
    _,public_key = load_keys()
    algorithm = data.get('algorithm')

    if not algorithm == 'RSA' and (not encrypted_message or not key or not algorithm):
        return Response({'error': 'Encrypted message, key, and algorithm are required'}, status=400)

    encrypted_message_record = EncryptedMessage.objects.filter(message=encrypted_message,algorithm=algorithm).first()
    if not encrypted_message_record:
        return Response({'error':'Encrypted message not found in the database'} , status=400)
    try:
       
        if algorithm == 'OTP':
            
            decrypted = otp_decrypt(encrypted_message, key)
        elif algorithm == 'DES3':
            decrypted = des3_decrypt(encrypted_message, key)
        elif algorithm == 'AES':
            decrypted = aes_decrypt(encrypted_message, key)
        elif algorithm == 'RSA':
            decrypted = rsa_decrypt(encrypted_message)
            key = serialize_rsa_key(public_key)
        else:
            return Response({'error': 'Invalid encryption algorithm'}, status=400)
    except ValueError as e:
        # Catch key mismatch or padding errors cleanly
        return Response({'error': f'Decryption failed: {str(e)}'}, status=400)
    except Exception as e:
        return Response({'error': f'Decryption failed: {str(e)}'}, status=400)

    return Response({'decrypted_message': decrypted,'encrypted_message':encrypted_message,'key':key,'algorithm':algorithm})