from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SuUserFollowing)
class SuUserFollowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'type', 'following', 'push_type',
                    'language', 'ut', 'aws_subscription')
