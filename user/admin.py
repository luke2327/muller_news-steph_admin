from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(SuUserFollowing)
class SuUserFollowingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'user_id', 'type', 'following', 'push_type',
                    'language', 'ut', 'aws_subscription')

@admin.register(SuAccountFollowing)
class SuAccountFollowingAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'account_id', 'type', 'following',
                    'push_type', 'ut')
@admin.register(SuTransaction)
class SuTransactionAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'user_id', 'account_id', 'login_ut', 'logout_ut')

@admin.register(SuAccount)
class SuAccountAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    list_display = ('id', 'email', 'password_', 'pf', 'pf_user_id',
                    'pf_user_name', 'pf_user_token_', 'pf_image_url_',
                    'email_confirmed', 'secret_key')

    def pf_user_token_(self, obj):
        return format_html("<div style='width: 1000px; word-break:break-word;'>{}</div>",
                            obj.pf_user_token)
    def password_(self, obj):
        if obj.password is None:
            return None
        else:
            return format_html("<div style='width: 100px; word-break:break-word;'>{}</div>",
                                obj.password)
    def pf_image_url_(self, obj):
        if obj.pf_image_url is None:
            return None
        else:
            return format_html("<div style='width: 300px; word-break:break-word;'>{}</div>",
                                obj.pf_image_url)
@admin.register(SuUser)
class SuUserAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_custom_default.html'
    list_display = ('del_field', 'id', 'device_id', 'create_tmp', 'language',
                    'os', 'push_key', 'aws_endpoint', 'last_login_ut')
