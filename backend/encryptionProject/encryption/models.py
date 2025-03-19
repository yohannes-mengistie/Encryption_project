from django.db import models

# Creating models
class EncryptedMessage(models.Model):
    ALGORITHM_CHOICES = [
        ('OTP','One-Time Pad'),
        ('3DES','Triple DES'),
        ('AES','AES Encryption'),
    ]

    message = models.TextField()
    decrypted_message = models.TextField(default="")
    plain_text = models.TextField()
    key = models.TextField()
    algorithm = models.CharField(max_length=10,choices = ALGORITHM_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.algorithm} - {self.created_at}"