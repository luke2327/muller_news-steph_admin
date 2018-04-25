from django.contrib import admin
from django import forms
from .models import *
from django.utils.html import format_html
from steph.util.util import Util
admin.site.empty_value_display = ''
# Register your models here.

@admin.register(SwipsBoardPost)
class SwipsBoardPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'participant', 'language',
                    'account_id', 'text_', 'img_ext', 'img_link', 'img_rot',
                    'img_width', 'img_height', 'create_time', 'edit_time_', 'del_field_')
    search_fields = ('del_field', 'type', 'participant', 'language', 'account_id',
                     'img_ext', 'img_rot', 'create_time', 'edit_time')
    list_filter = ('type', 'participant', 'language', 'account_id',
                      'img_ext', 'img_rot', 'create_time', 'edit_time')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def img_link(self, obj):
        if obj.img_ext is None:
            return None;
        else:
            return format_html("<a href='http://board.swips.co/origin/bo/te_{}_{}.{}'>\
            <img src='http://board.swips.co/thumbnails/origin/bo/te_{}_{}.jpg'></a>",
            obj.participant, obj.id, obj.img_ext, obj.participant, obj.id)
    def text_(self, obj):
        return format_html("<div style='width: 500px; word-break:break-word;'>{}</div>", obj.text)
    def edit_time_(self,obj):
        if obj.edit_time == '0000-00-00 00:00:00':
            return None
        else:
            return obj.edit_time
    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_board_post', 'id', obj.id,\
                           'del', obj.del_field, 'text')
@admin.register(SwipsBoardReply)
class SwipsBoardReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'participant', 'account_id',
                    'post_id', 'root_type', 'root_id', 'text', 'create_time',
                    'edit_time', 'language', 'del_field_',)
    search_fields = ('type', 'participant', 'language',
                              'account_id', 'post_id', 'root_type', 'root_id',
                              'text', 'create_time', 'edit_time')
    list_filter = ('type', 'participant', 'language', 'account_id',
                      'post_id', 'root_type', 'root_id', 'text', 'create_time',
                      'edit_time')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_board_reply', 'id', obj.id,\
                           'del', obj.del_field, 'text')
@admin.register(SwipsBoardLike)
class SwipsBoardLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'root_id', 'account_id', 'create_time')
    search_fields = ('type', 'root_id', 'account_id', 'create_time')
    list_filter = ('type', 'root_id', 'account_id', 'create_time')
    change_list_template = 'admin/steph_admin/change_list_custom.html'
