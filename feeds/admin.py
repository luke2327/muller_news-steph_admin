from django.contrib import admin
from django.forms import BaseModelFormSet, TextInput, Textarea
from django import forms
# Register your models here.
from .models import *
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars
from steph.util.util import Util
from datetime import datetime
class CurryNewsAdmin(admin.ModelAdmin):
    #list_display = ('id','ut','ut2','name','country','date_of_birth','position','status')
    list_display = ('id','push','lang','source_','link_news','link_image',\
                'is_frifee_content_', 'pushed_', 'del_field_',\
                'create_tmp_','is_top','sport','title_','following_desc_',\
                'following_')
    list_filter = ['language_cd', 'del_field','create_tmp','sport','is_frifee_content']
    #list_editable = ['sport','source', 'create_tmp', 'is_top']
    search_fields = ['title', 'following_desc','source']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_news.html'

    def push(self, obj):
        datas = []
        try :
            for row in obj.le_relation.split(',') :
                datas.append('League/%s' % row)
        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                datas.append('Team/%s' % row)
        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                datas.append('Player/%s' % row)
        except Exception as e :
            pass
        return format_html('<a class="btn news_push glyphicon glyphicon-send" id="push-%s" datas = "%s" title="%s" lang="%s"></a>' %(obj.id, ','.join(datas), obj.title, obj.language_cd))
    def changelist_view(self, request, extra_context=None):
        extra = {}
        extra['players'] = 'messi'
        extra['h'] = {}
        print(extra_context)
        return super(CurryNewsAdmin, self).changelist_view(request, extra_context=extra)
    def lang(self, obj):
        return obj.language_cd
    def link_news(self, obj):
        return format_html("<a target='_blank' href='{0}'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a target='_blank' href='{0}'>click</a>", obj.image_link)
    def title_(self, obj):
        return format_html('<div title = "{}" style="width:300px; word-break:break-word;">{}<div>', obj.title, obj.title)
    def following_desc_(self, obj):
        return format_html('<div title = "{}" style="width:300px; word-break:break-word;">{}<div>', obj.following_desc, obj.following_desc)
        #return truncatechars(obj.following_desc, 100)
    def following_(self, obj) :
        html = '<ul class = "list-unstyled" id = "following_%s">' %(obj.id)
        html += '<li><a class="btn btn-primary btn-sm following_add" style="margin-bottom: 5px;" data_id="%s">+ following add</a></li>' %(obj.id)
        try :
            for row in obj.le_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        html += '</ul>'
        return format_html(html)
    def source_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'source', obj.source, 'text')
    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'del', obj.del_field, 'text')
    def pushed_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'pushed', obj.pushed, 'text')
    def is_frifee_content_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'is_frifee_content', obj.is_frifee_content, 'text')
    def create_tmp_(self, obj):
        formated = obj.create_tmp.strftime("%Y-%m-%d %H:%M:%S")
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'create_tmp', formated, 'text')
class CurryVodAdmin(admin.ModelAdmin):
    list_display = ('id','push','match_id_','lang','source','link_news','link_image',\
                'is_frifee_content_', 'pushed_', 'del_field_',\
                'create_tmp','is_top','sport','country_cd','country_exclude_cd','is_live','title_','following_desc_',\
                'following_')
    list_filter = ['language_cd', 'del_field','create_tmp','sport']
    search_fields = ['title', 'following_desc','source']
    # list_editable = ['title_']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_vods.html'
    def push(self, obj):
        datas = []
        try :
            for row in obj.le_relation.split(',') :
                datas.append('League/%s' % row)
        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                datas.append('Team/%s' % row)
        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                datas.append('Player/%s' % row)
        except Exception as e :
            pass
        return format_html('<a class="btn news_push glyphicon glyphicon-send" id="push-%s" datas = "%s" title="%s" lang="%s"></a>' %(obj.id, ','.join(datas), obj.title, obj.language_cd))
    def lang(self, obj):
        return obj.language_cd
    def link_news(self, obj):
        return format_html("<a href='{0}'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}'>click</a>", obj.image_link)
    def title_(self, obj):
        return format_html('<div title = "{}" style="width:300px; word-break:break-word;">{}<div>', obj.title, obj.title)
    def following_desc_(self, obj):
        return format_html('<div title = "{}" style="width:300px; word-break:break-word;">{}<div>', obj.following_desc, obj.following_desc)
        #return truncatechars(obj.following_desc, 100)
    def following_(self, obj) :
        html = '<ul class = "list-unstyled" id = "following_%s">' %(obj.id)
        html += '<li><a class="btn btn-primary btn-sm following_add" style="margin-bottom: 5px;" data_id="%s">+ following add</button></li>' %(obj.id)
        try :
            for row in obj.le_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        html += '</ul>'
        return format_html(html)
    def is_frifee_content_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'is_frifee_content', obj.is_frifee_content, 'text')
    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'del', obj.del_field, 'text')
    def pushed_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'pushed', obj.pushed, 'text')
    def match_id_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'match_id', obj.match_id, 'text')
@admin.register(SwipsCrawlingSource)
class SwipsCrawlingSourceAdmin(admin.ModelAdmin):
    list_display = ('del_field_', 'id', 'source_', 'content_type', 'sport',
                    'language_cd', 'frequency_cl', 'importance_cl', 'ut')

    list_editable = ['frequency_cl', 'importance_cl']
    list_display_links = ['id',]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def source_(self, obj):
        return Util().get_popover('admin', 'swips_crawling_source', 'id', obj.id,\
                           'source', obj.source, 'text')
    def del_field_(self, obj):
        return Util().get_popover('admin', 'swips_crawling_source', 'id', obj.id,\
                           'del_field', obj.del_field, 'text')
admin.site.register(CurryVod,CurryVodAdmin)
admin.site.register(CurryNews,CurryNewsAdmin)
