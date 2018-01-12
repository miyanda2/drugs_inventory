from django.contrib import admin

# Register your models here.
from .models import Drug
from .models import issued_Drug

admin.site.register(Drug)
admin.site.register(issued_Drug)
#admin.site.register(Step)
#search_fields = ['Drug_name']
