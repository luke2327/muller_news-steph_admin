from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(SwipsTransfer)
class SwipsTransferAdmin(admin.ModelAdmin):
    change_list_template = 'admin/steph_admin/change_list_transfer.html'
    list_display = ('id', 'push_send', 'sport', 'player_id', 'player_name', 'position',
                    'from_team_id', 'from_team_name', 'to_team_id',
                    'to_team_name', 'is_loan', 'type', 'contract_dt',
                    'contract_info', 'fee', 'fee_info', 'fee_currency',
                    'ut', 'source_link_id', 'source_link_th', 'source_link_pt',
                    'source_link_ko', 'source_link_vi', 'source_link_en')

    list_filter = ['sport' , 'player_id', 'from_team_id', 'to_team_id',
                      'is_loan', 'type']
    search_fields = ['player_id', 'player_name', 'from_team_id',
                      'from_team_name', 'to_team_id', 'to_team_name']

    def push_send(self, obj):
        return format_html('<ul class = "list-unstyled">'
                           '<li><a class="grp-button transfer_push_send" data="0,%s,%s,%s,%s,%s,%s,%s">from_team</a><li>'
                           '<li><a class="grp-button transfer_push_send" data="1,%s,%s,%s,%s,%s,%s,%s">to_team</a><li>'
                           '</ul>'
                           %(obj.from_team_id, obj.id, obj.player_name, obj.from_team_name, obj.to_team_name, obj.type, obj.is_loan,
                            obj.to_team_id, obj.id, obj.player_name, obj.from_team_name, obj.to_team_name, obj.type, obj.is_loan))
    def source_linker(self, object):
        return format_html("<a href='{}' target='_blank'>{}</a>", object, object)

    def source_link_id(self, obj):
        if obj.source_id is None:
            return None
        else:
            return self.source_linker(obj.source_id)
    def source_link_th(self, obj):
        if obj.source_th is None:
            return None
        else:
            return self.source_linker(obj.source_th)
    def source_link_pt(self, obj):
        if obj.source_pt is None:
            return None
        else:
            return self.source_linker(obj.source_pt)
    def source_link_ko(self, obj):
        if obj.source_ko is None:
            return None
        else:
            return self.source_linker(obj.source_ko)
    def source_link_vi(self, obj):
        if obj.source_vi is None:
            return None
        else:
            return self.source_linker(obj.source_vi)
    def source_link_en(self, obj):
        if obj.source_en is None:
            return None
        else:
            return self.source_linker(obj.source_en)
