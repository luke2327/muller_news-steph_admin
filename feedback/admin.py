from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SwipsFeedback)
class SwipsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_agent', 'language',
                    'feedback', 'email', 'ut', 'status')
