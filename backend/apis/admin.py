from django.contrib import admin
from apis import models

# Register your models here.
@admin.register(models.Article)
class Admin(admin.ModelAdmin):
    list_display = ['user', 'title']
    
