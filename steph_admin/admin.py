from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
class CurryNewsAdmin(admin.ModelAdmin):

    #list_display = ('id','ut','ut2','name','country','date_of_birth','position','status')
    list_display = ('id','lang','source','link_news','link_image',\
                'is_frifee_content', 'pushed', 'del_field',\
                'create_tmp','is_top','sport','title_','following_desc_',\
                'following_')
    list_filter = ['language_cd', 'del_field','create_tmp','sport']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_custom.html'

    # def get_queryset(self, request):
    #     return CurryNews.objects.all()
        # return SwipsNews.objects.raw(\
        # 'SELECT '
        # '`sn`.`id` AS `id`, '
        # '`sn`.`language_cd` AS `language_cd`, '
        # '`sn`.`link` AS `link`, '
        # '`sn`.`image_link` AS `image_link`, '
        # '`sn`.`create_tmp` AS `create_tmp`, '
        # '`sn`.`is_top` AS `is_top`, '
        # '`sn`.`sport` AS `sport`, '
        # '`sn`.`title` AS `title`, '
        # '`sn`.`source` AS `source`, '
        # '`sn`.`is_frifee_content` AS `is_frifee_content`, '
        # '`sn`.`pub_date` AS `pub_date`, '
        # '`sn`.`following_desc` AS `following_desc`, '
        # '`sn`.`pushed` AS `pushed`, '
        # '`sn`.`del` AS `del`, '
        # 'GROUP_CONCAT(`spi`.`name`, "/", `spi`.`player`'
        # '   SEPARATOR ",") AS `pl_relation`,'
        # 'GROUP_CONCAT(`sti`.`name`, "/", `sti`.`team`'
        # '    SEPARATOR ",") AS `te_relation`,'
        # 'GROUP_CONCAT(`sli`.`name`, "/", `sli`.`league`'
        # '    SEPARATOR ",") AS `le_relation`'
        # 'FROM'
        # '((((`swips_news` `sn` '
        # 'LEFT JOIN `swips_news_relation` `snr` ON ((`sn`.`id` = `snr`.`news_id`))) '
        # 'LEFT JOIN `swips_player_info` `spi` ON ((`spi`.`player` = `snr`.`participant`))) '
        # 'LEFT JOIN `swips_team_info` `sti` ON ((`sti`.`team` = `snr`.`participant`))) '
        # 'LEFT JOIN `swips_league_info` `sli` ON ((`sli`.`league` = `snr`.`participant`))) '
        # 'GROUP BY `sn`.`id` '
        # 'ORDER BY `sn`.`id` DESC '
        # 'LIMIT 3000').all()
    def changelist_view(self, request, extra_context=None):
        extra = {}
        extra['players'] = 'messi'
        extra['h'] = {}
        print(extra_context)
        return super(CurryNewsAdmin, self).changelist_view(request, extra_context=extra)
    def lang(self, obj):
        return obj.language_cd
    def link_news(self, obj):
        return format_html("<a href='{0}'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}'>click</a>", obj.image_link)
    def title_(self, obj):
        return format_html('<div title = "{}">{}<div>', obj.title, truncatechars(obj.title, 50))
    def following_desc_(self, obj):
        return format_html('<div title = "{}">{}<div>', obj.following_desc, obj.following_desc)
        #return truncatechars(obj.following_desc, 100)
    def following_(self, obj) :
        html = '<ul>'
        html += '<li><a class="button" data-toggle="modal" data-target="#myModal">following add</button></li>'
        try :
            for row in obj.le_relation.split(',') :
                html = html + '<li><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s">%s</a></li>' %(row,row)

        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                html = html + '<li><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s">%s</a></li>' %(row,rwo)

        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                html = html + '<li><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s">%s</a></li>' %(row,row)

        except Exception as e :
            pass
        html += '</ul>'
        return format_html(html)
admin.site.register(CurryNews,CurryNewsAdmin)
admin.site.register(SwipsPlayer)
