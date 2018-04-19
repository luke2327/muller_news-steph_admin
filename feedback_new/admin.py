from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(SwipsQna)
class SwipsQnaAdmin(admin.ModelAdmin):
    list_display = ('field_del', 'id', 'user_id', 'account_id', 'user_agent', 'language',
                    'feedback', 'img_link', 'answer', 'ut', 'answer_ut', 'status')

    def img_link(self, obj):
        if obj.img_ext is None:
            return None
        else:
            return format_html("<a href='http://board.swips.co/origin/feedback/{}.jpg'>\
            <img src='http://board.swips.co/thumbnails/origin/feedback/{}.jpg'></a>",
            obj.id, obj.id)
