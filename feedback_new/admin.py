from django.contrib import admin
from .models import *
from django.utils.html import format_html
from steph.util.util import Util
# Register your models here.

@admin.register(SwipsQna)
class SwipsQnaAdmin(admin.ModelAdmin):
    list_display = ('id', 'del_field_', 'user_id', 'account_id', 'user_agent', 'language',
                    'feedback', 'img_link', 'answer_', 'ut', 'answer_ut_', 'status_')
    list_display_links = ['id',]
    search_fields = ['id', 'user_id', 'account_id', 'user_agent', 'feedback', 'answer', 'language', 'status']
    list_filter = ('language', 'status',  'user_id', 'account_id')
    change_list_template = 'admin/steph_admin/change_list_feedback_new.html'
    def img_link(self, obj):
        if obj.img_ext is None:
            return None
        else:
            return format_html("<a href='http://board.swips.co/origin/feedback/%s.%s'>\
            <img src='http://board.swips.co/thumbnails/origin/feedback/%s.jpg'></a>"
            %(obj.id, obj.img_ext, obj.id))

    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_qna', 'id', obj.id,\
                           '_del', obj.field_del, 'text')

    def answer_(self, obj):
        return Util().get_popover('admin', 'swips_qna', 'id', obj.id,\
                           'answer', obj.answer, 'textarea')

    def answer_ut_(self, obj):
        return Util().get_popover('admin', 'swips_qna', 'id', obj.id,\
                           'answer_ut', obj.answer_ut, 'text')

    def status_(self, obj):
        return Util().get_popover('admin', 'swips_qna', 'id', obj.id,\
                           'status', obj.status, 'text')
