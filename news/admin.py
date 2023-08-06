from django.contrib import admin
from news.models import headline

# CHANGING TABLE LAYOUT
class headlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# Register your models here.
admin.site.register(headline, headlineAdmin)