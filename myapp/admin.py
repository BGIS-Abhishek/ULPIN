from django.contrib import admin
from .models import Files,Locations,MyPIN

# Register your models here.
admin.site.register(Files)
admin.site.register(Locations)
admin.site.register(MyPIN)