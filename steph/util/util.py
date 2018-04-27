from django.utils.html import format_html
class Util():
    @staticmethod
    def get_popover(db_type, table, primary_key, primary_value,\
                    change_key, default_value, edit_type, list=[]):

        return format_html('<a href="#" '
                           'class = "edit_pop_%s" '
                           'data-db_type="%s" '
                           'data-table="%s" '
                           'data-primary_key="%s" '
                           'data-primary_value="%s" '
                           'data-change_key="%s" '
                           'data-default_value="%s" '
                           'data-type="%s" '
                           'data-list="%s" '
                           'id = "%s%s%s"'
                           '>%s</a>'
                           %(edit_type, db_type, table, primary_key, primary_value,\
                            change_key, default_value, edit_type, ','.join(list),\
                            primary_key, primary_value, change_key, default_value  if default_value != None else ''))

    @staticmethod
    def get_count_change(db_type, table, primary_key, primary_value,\
                    change_key, default_value, edit_type, max_value=1):
        return format_html('<span href="" '
                           'class = "edit_count_%s" '
                           'data-db_type="%s" '
                           'data-table="%s" '
                           'data-primary_key="%s" '
                           'data-primary_value="%s" '
                           'data-change_key="%s" '
                           'data-default_value="%s" '
                           'data-type="%s" '
                           'data-max="%s" '
                           'id = "%s%s%s"'
                           'style="color: #337ab7; text-decoration: underline; cursor: pointer;"'
                           '>%s</span>'
                           %(edit_type, db_type, table, primary_key, primary_value,\
                            change_key, default_value, edit_type, max_value,\
                            primary_key, primary_value, change_key, default_value))
