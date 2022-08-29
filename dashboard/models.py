from django.db import models
from authz.models import User
import secrets

# Create your models here.
class Payment(models.Model):
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ("-date_created" )

    def __str__(self) -> str:
        return f"Payment: {self.ref}"
