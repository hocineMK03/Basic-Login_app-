from django.contrib import admin

# Register your models here.
from .models import Customers,Session_model

admin.site.register(Customers)
admin.site.register(Session_model)