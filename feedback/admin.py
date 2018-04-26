from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SwipsFeedback)
class SwipsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_agent', 'language',
                    'feedback', 'email', 'ut', 'status')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
<<<<<<< HEAD
    def has_add_permission(self, request):
        return False
=======
    list_filter = ['language', 'status']
    search_fields = ['feedback', 'email']
>>>>>>> a1fc3494c1418b913508a4827df667d00c5ab557
