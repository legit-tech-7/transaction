from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import uuid

class Transaction(models.Model):
    # Transaction Reference
    transaction_ref = models.CharField(max_length=50, unique=True, editable=False)
    
    # Sender Details
    sender_name = models.CharField(max_length=200)
    sender_account = models.CharField(max_length=20)
    sender_country = models.CharField(max_length=100)
    
    # Receiver Details
    receiver_name = models.CharField(max_length=200)
    receiver_account = models.CharField(max_length=20)
    receiver_country = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    receiver_bank = models.CharField(max_length=50)
    
    # Transaction Details
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.transaction_ref:
            self.transaction_ref = self.generate_transaction_ref()
        super().save(*args, **kwargs)
    
    def generate_transaction_ref(self):
        """Generate unique transaction reference matching the format in the image"""
        timestamp = timezone.now().strftime('%y%m%d%H%M%S')
        unique_id = str(uuid.uuid4().hex)[:12].upper()
        return f"NXG0000{timestamp}{unique_id}"
    
    def __str__(self):
        return self.transaction_ref