from django.contrib import admin
from .models import TaskerWallet, PaymentMethod, CustomerWallet

admin.site.register(TaskerWallet)
admin.site.register(CustomerWallet)
admin.site.register(PaymentMethod)

# Register your models here.
