from django.contrib import admin
from .models import Payment, Withdraw, Transfer
# Register your models here.
admin.site.register(Payment)
admin.site.register(Withdraw)
admin.site.register(Transfer)