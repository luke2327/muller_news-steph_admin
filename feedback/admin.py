from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SwipsFeedback)
class SwipsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_agent', 'language',
                    'feedback', 'email', 'ut', 'status')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    
    def has_add_permission(self, request):
        return False
    list_filter = ['language', 'status']
    search_fields = ['feedback', 'email']
