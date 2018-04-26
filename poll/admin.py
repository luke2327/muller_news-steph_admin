from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(SwipsPoll)
class SwipsPollAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'number', 'type', 'participant', 'ut')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    search_fields = ['item', 'participant', 'type']
    list_filter = ['item', 'participant', 'type']
    def has_add_permission(self, request):
        return False

@admin.register(SwipsBoard)
class SwipsBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'type', 'participant', 'language',
                    'text_', 'ut', 'account_id')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    search_fields = ('item', 'participant', 'language', 'account_id',
                              'text', 'type')
    list_filter = ['item', 'participant', 'language', 'account_id', 'type']
    def text_(self, obj):
        if obj.text is None:
            return None
        else:
            return format_html("<div style='width: 500px;\
            word-break:break-word;'>{}</div>", obj.text)
            
    def has_add_permission(self, request):
        return False
    search_fields = ['item', 'participant', 'language', 'account_id',
                    'text', 'type']
    list_filter = ['item', 'participant', 'language', 'account_id', 'type']
