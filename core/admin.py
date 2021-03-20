from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=['msg_id','name','email','contact','message','subject']

admin.site.register(Contact,ContactAdmin)