from django.contrib import admin
from django import forms
from .models import *
from django.utils.html import format_html

# Register your models here.

@admin.register(SwipsBoardPost)
class SwipsBoardPostAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'type', 'participant', 'language',
                    'account_id', 'text', 'img_ext', 'img_link', 'img_rot',
                    'img_width', 'img_height', 'create_time', 'edit_time')

    def img_link(self, obj):
        return format_html("<a href='http://board.swips.co/origin/bo/te_{}_{}.{}'>\
        <img src='http://board.swips.co/thumbnails/origin/bo/te_{}_{}.{}'</a>",
         obj.participant, obj.id, obj.img_ext, obj.participant, obj.id, obj.img_ext)

@admin.register(SwipsBoardReply)
class SwipsBoardReplyAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'type', 'participant', 'account_id',
                    'post_id', 'root_type', 'root_id', 'text', 'create_time',
                    'edit_time', 'language')
                    
@admin.register(SwipsBoardLike)
class SwipsBoardLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'root_id', 'account_id', 'create_time')
