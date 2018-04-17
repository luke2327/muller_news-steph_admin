class MultiDBRouter(object):
    def db_for_read(self, model, **hints):
        print('db_for_read')
        print(model._meta.app_label)
        if model._meta.app_label == 'steph_admin' or \
            model._meta.app_label == 'feeds' or \
            model._meta.app_label == 'lineup' or \
            model._meta.app_label == 'preview_review':

            return 'admin'

        return 'users'

    def db_for_write(self, model, **hints):
        print('db_for_write')
        print(model._meta.app_label)
        if model._meta.app_label == 'steph_admin' or \
            model._meta.app_label == 'feeds' or\
            model._meta.app_label == 'lineup' or\
            model._meta.app_label == 'preview_review':
            return 'admin'
        return 'users'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'steph_admin': return False
        else : return True
