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
    list_editable = ['sport','source', 'create_tmp', 'is_top']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_news.html'

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

class CurryVodAdmin(admin.ModelAdmin):
    list_display = ('id','match_id','lang','source','link_news','link_image',\
                'is_frifee_content', 'pushed', 'del_field',\
                'create_tmp','is_top','sport','country_cd','country_exclude_cd','is_live','title_','following_desc_',\
                'following_')
    list_filter = ['language_cd', 'del_field','create_tmp','sport']
    # list_editable = ['title_']
    '''
    display_as_charfield = ['name', 'country']
    '''
    list_per_page = 20
    change_list_template = 'admin/steph_admin/change_list_vods.html'

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

@admin.register(SwipsCrawlingSource)
class SwipsCrawlingSourceAdmin(admin.ModelAdmin):
    list_display = ('del_field', 'id', 'source', 'content_type', 'sport',
                    'language_cd', 'frequency_cl', 'importance_cl', 'ut')

    list_editable = ['del_field','frequency_cl', 'importance_cl']
    list_display_links = ['source',]

admin.site.register(CurryVod,CurryVodAdmin)
admin.site.register(CurryNews,CurryNewsAdmin)
