from django.db import models
from authz.models import User
import secrets

# Create your models here.
class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    acc = models.PositiveIntegerField()
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ("-date_created" )

    def __str__(self) -> str:
        return f"Payment: {self.ref}"

class Withdraw(models.Model):
    email = models.EmailField()
    account = models.PositiveIntegerField()
    ref = models.CharField(max_length=200 , default="007")
    amount = models.CharField(max_length=30)
    beneficiary_fullname = models.CharField(max_length=200)
    beneficiary_address = models.CharField(max_length=200)
    beneficiary_city = models.CharField(max_length=200)
    beneficiary_zip = models.CharField(max_length=200)
    beneficiary_country = models.CharField(max_length=200)
    bank_account = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)
    branch_code = models.CharField(max_length=200)
    bank_address = models.CharField(max_length=200)
    beneficiary_swift = models.CharField(max_length=200)
    bic = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"Withraw: {self.email}"


class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ref = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    date2 = models.DateTimeField(auto_now_add=True)
    sent_from = models.CharField(max_length=20)
    sent_to = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"transfer: {self.ref}"