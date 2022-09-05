from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    language = models.CharField(max_length=50)
    existing= models.CharField(max_length=5)
    phone_num= models.CharField(max_length=20,null=True)
    account_number = models.CharField(max_length=20,null=True)
    enquiry_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    attended_to = models.BooleanField(default=False)

    def __str__(self):
        if len(self.message) < 15:
            return self.message
        return self.text[:11] + ' ...'