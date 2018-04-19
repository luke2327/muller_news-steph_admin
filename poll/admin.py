from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(SwipsPoll)
class SwipsPollAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'number', 'type', 'participant', 'ut')

@admin.register(SwipsBoard)
class SwipsBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'type', 'participant', 'language',
                    'text_', 'ut', 'account_id')
    def text_(self, obj):
        if obj.text is None:
            return None
        else:
            return format_html("<div style='width: 500px;\
            word-break:break-word;'>{}</div>", obj.text)
