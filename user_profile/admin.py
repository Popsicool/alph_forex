from django.contrib import admin
from .models import Document, Change_document_request, Account
# Register your models here.
admin.site.register(Document)
admin.site.register(Change_document_request)
admin.site.register(Account)
