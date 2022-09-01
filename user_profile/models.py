from django.db import models
from authz.models import User

# Create your models here.
class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    nationality = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    dob_dd = models.CharField(max_length=20)
    tin = models.CharField(max_length=30)
    tax_country = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    postcode = models.IntegerField()
    country = models.CharField(max_length=200)
    phone_landline = models.CharField(max_length=20)
    phone_mobile = models.CharField(max_length=20)
    employment_status = models.CharField(max_length=20, default= None )
    business_nature =models.CharField(max_length=50)
    funds_source = models.CharField(max_length=50)
    expected_deposit_id = models.CharField(max_length=50)
    annual_income = models.CharField(max_length=50)
    net_worth = models.CharField(max_length=50)
    traded_forex = models.IntegerField()
    traded_forex_frequency = models.CharField(max_length=20)
    traded_forex_volume = models.CharField(max_length=50)
    traded_bonds_frequency = models.CharField(max_length=20)
    traded_bonds_volume = models.CharField(max_length=50)
    traded_products_frequency = models.CharField(max_length=50)
    traded_products_volume = models.CharField(max_length=50)
    seminar_experience = models.CharField(max_length=5)
    seminar_course_experience = models.CharField(max_length=200)
    work_experiencework_experience = models.CharField(max_length=5)
    work_qualification_experience = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        # show how we want it to be displayed
        return f"{self.user.email}'s Document"
    
class Change_document_request(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        # show how we want it to be displayed
        return f"{self.user.email}'s Request"


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=15)
    currency_base = models.CharField(max_length=5)
    bonus_category = models.CharField(max_length=50)
    leverage = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)

    def __str__(self):
        # show how we want it to be displayed
        return f"{self.account_number}"
