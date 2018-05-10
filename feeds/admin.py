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
                'create_tmp_','is_top_','sport_','title_','following_desc_',\
                'following_')
    list_filter = ['source', 'sport', 'is_top', 'is_frifee_content', 'language_cd', 'del_field', 'pushed']
    #list_editable = ['sport','source', 'create_tmp', 'is_top']
    search_fields = ['id', 'title', 'following_desc','source']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_news.html'
    list_display_links = None

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False
    actions = ['del_field_change', ]

    def del_field_change(self, request, queryset):
        ids_del = []
        ids = []
        for row in queryset :
            if row.del_field is None or row.del_field == 0 :
                ids_del.append(str(row.id))
            else :
                ids.append(str(row.id))
        SwipsNews.objects.filter(id__in=ids).all().update(del_field = 0)
        SwipsNews.objects.filter(id__in=ids_del).all().update(del_field = 1)
    del_field_change.short_description = "선택한 뉴스 del값을 바꿉니다"
    def get_actions(self, request):

        actions = super(CurryNewsAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
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
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.image_link)
    def title_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'title', obj.title, 'textarea')
    def following_desc_(self, obj):
        return format_html('<div title = "{}" style="width:300px; word-break:break-word;">{}<div>', obj.following_desc, obj.following_desc)
        #return truncatechars(obj.following_desc, 100)
    def following_(self, obj) :
        html = '<ul class = "list-unstyled" id = "following_%s">' %(obj.id)
        html += '<li><a class="btn btn-primary btn-sm following_add" style="margin-bottom: 5px;" data_id="%s">+ following add</a></li>' %(obj.id)
        try :
            for row in obj.le_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_le" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_te" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)
        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_pl" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        html += '</ul>'
        return format_html(html)
    def source_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'source', obj.source, 'text')
    def del_field_(self, obj):
        return Util().get_count_change('admin', 'swips_news', 'id', obj.id,\
                           'del', obj.del_field, 'text')
    def is_frifee_content_(self, obj):
        return Util().get_count_change('admin', 'swips_news', 'id', obj.id,\
                           'is_frifee_content', obj.is_frifee_content, 'text', 2)
    def create_tmp_(self, obj):
        formated = obj.create_tmp.strftime("%Y-%m-%d %H:%M:%S")
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'create_tmp', formated, 'text')
    def is_top_(self, obj):
        return Util().get_count_change('admin', 'swips_news', 'id', obj.id,\
                           'is_top', obj.is_top, 'text', 2)
    def sport_(self, obj):
        return Util().get_popover('admin', 'swips_news', 'id', obj.id,\
                           'sport', obj.sport, 'text')
    def pushed_(self, obj):
        return format_html('<span id="%s%s%s">%s</span>' %('id', obj.id, 'pushed', obj.pushed))
    def has_add_permission(self, request):
        return False
class CurryVodAdmin(admin.ModelAdmin):
    list_display = ('id','push','match_id_','lang','source','link_vods','link_image',\
                'is_frifee_content_', 'pushed_', 'del_field_',\
                'create_tmp','is_top_','sport_','country_cd_','country_exclude_cd_','is_live_','title_','following_desc_',\
                'following_')
    list_filter = ['source', 'sport', 'is_top', 'is_live', 'language_cd', 'country_cd', 'country_exclude_cd', 'del_field']
    search_fields = ['id', 'title', 'source', 'following_desc']
    # list_editable = ['title_']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    actions = ['del_field_change', ]
    list_display_links = None
    change_list_template = 'admin/steph_admin/change_list_vods.html'
    def del_field_change(self, request, queryset):
        print('delf_field_0')
        ids_del = []
        ids = []
        for row in queryset :
            if row.del_field is None or row.del_field == 0 :
                ids_del.append(str(row.id))
            else :
                ids.append(str(row.id))
        SwipsVod.objects.filter(id__in=ids).all().update(del_field = 0)
        SwipsVod.objects.filter(id__in=ids_del).all().update(del_field = 1)
    del_field_change.short_description = "선택한 VOD del값을 바꿉니다"

    def get_actions(self, request):

        actions = super(CurryVodAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
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
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'language_cd', obj.language_cd, 'text')
    def link_vods(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.image_link)
    def title_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'title', obj.title, 'textarea')

    def following_desc_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'following_desc', obj.following_desc, 'textarea')
    def following_(self, obj) :
        html = '<ul class = "list-unstyled" id = "following_%s">' %(obj.id)
        html += '<li><a class="btn btn-primary btn-sm following_add" style="margin-bottom: 5px;" data_id="%s">+ following add</button></li>' %(obj.id)
        try :
            for row in obj.le_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_le" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e:
            print(e)
            pass
        try :
            for row in obj.te_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_te" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        try :
            for row in obj.pl_relation.split(',') :
                html = html + '<li id = "f_add_%s_%s" ><a data-toggle="modal" data-target="#del_following" class="following_del following_pl" following="%s" data_id="%s">%s</a></li>' %(obj.id,row.split('/')[1],row,obj.id,row)

        except Exception as e :
            pass
        html += '</ul>'
        return format_html(html)
    def is_frifee_content_(self, obj):
        return Util().get_count_change('admin', 'swips_vod', 'id', obj.id,\
                           'is_frifee_content', obj.is_frifee_content, 'text')
    def del_field_(self, obj):
        return Util().get_count_change('admin', 'swips_vod', 'id', obj.id,\
                           'del', obj.del_field, 'text')
    def match_id_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'match_id', obj.match_id, 'text')
    def is_top_(self, obj):
        return Util().get_count_change('admin', 'swips_vod', 'id', obj.id,\
                           'is_top', obj.is_top, 'text', 2)
    def sport_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'sport', obj.sport, 'text')
    def country_cd_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'country_cd', obj.country_cd, 'text')
    def country_exclude_cd_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'country_exclude_cd', obj.country_exclude_cd, 'text')
    def is_live_(self, obj):
        return Util().get_popover('admin', 'swips_vod', 'id', obj.id,\
                           'is_live', obj.is_live, 'text')
    def pushed_(self, obj):
        return format_html('<span id="%s%s%s">%s</span>' %('id', obj.id, 'pushed', obj.pushed))
    def has_add_permission(self, request):
        return False
@admin.register(SwipsCrawlingSource)
class SwipsCrawlingSourceAdmin(admin.ModelAdmin):
    list_display = ('del_field_', 'id', 'source_', 'content_type', 'sport',
                    'language_cd', 'frequency_cl', 'importance_cl', 'description', 'ut')
    list_filter = ['source', 'content_type', 'sport', 'language_cd',
                      'frequency_cl', 'importance_cl', 'ut', 'del_field']
    list_editable = ['frequency_cl', 'importance_cl', 'description']
    list_display_links = ['id',]
    change_list_template = 'admin/steph_admin/change_list_custom.html'
    def has_add_permission(self, request):
        return False

    def source_(self, obj):
        return Util().get_popover('admin', 'swips_crawling_source', 'id', obj.id,\
                           'source', obj.source, 'text')
    def del_field_(self, obj):
        return Util().get_count_change('admin', 'swips_crawling_source', 'id', obj.id,\
                           'del', obj.del_field, 'text')
@admin.register(SwipsNews)
class SwipsNewsAdmin(admin.ModelAdmin):
    list_display = ('id','language_cd','source','link_news','link_image',\
                    'is_frifee_content', 'pushed', 'del_field',\
                    'create_tmp','is_top','sport','title','following_desc')
    list_filter = ['source', 'sport', 'is_top', 'is_frifee_content', 'language_cd', 'del_field', 'pushed']
    search_fields = ['id', 'title', 'source', 'following_desc']
    change_list_template = 'admin/steph_admin/change_list_news.html'
    def link_news(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.image_link)
@admin.register(SwipsVod)
class SwipsVodAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id', 'link_news', 'link_image', 'create_tmp', 'is_top', 'sport', 'country_cd', 'language_cd', 'title', 'source', 'following_desc', 'is_frifee_content', 'pushed', 'country_exclude_cd', 'del_field', 'is_live')
    list_filter = ['source', 'sport', 'is_top', 'is_live', 'language_cd', 'country_cd', 'country_exclude_cd', 'del_field']
    search_fields = ['id', 'title', 'source', 'following_desc']
    change_list_template = 'admin/steph_admin/change_list_vods.html'
    def link_news(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.link)
    def link_image(self, obj):
        return format_html("<a href='{0}' target='_blank'>click</a>", obj.image_link)
admin.site.register(CurryVod,CurryVodAdmin)
admin.site.register(CurryNews,CurryNewsAdmin)
