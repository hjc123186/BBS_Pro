from django.contrib import admin
from app01.models import BBS,BBS_user,Category

class BBSAdmin(admin.ModelAdmin):
    list_display = ['title','summary','author','view_count','created_at']
    list_filter = ('created_at',)
    search_fields = ('title','author_user_username')

admin.site.register(BBS,BBSAdmin)
admin.site.register(Category)
admin.site.register(BBS_user)