class MultiDBRouter(object):
    def db_for_read(self, model, **hints):
        print('db_for_read')
        print(model._meta.app_label)
        if model._meta.app_label == 'steph_admin' or \
            model._meta.app_label == 'feeds' or \
            model._meta.app_label == 'lineup' or \
            model._meta.app_label == 'league_team_player' or \
            model._meta.app_label == 'preview_review' or \
            model._meta.app_label == 'board' or \
            model._meta.app_label == 'feedback' or \
            model._meta.app_label == 'feedback_new' or \
            model._meta.app_label == 'transfer' or \
            model._meta.app_label == 'user' or \
            model._meta.app_label == 'etc' or \
            model._meta.app_label == 'event' or \
            model._meta.app_label == 'poll' or \
            model._meta.app_label == 'info_update' or \
            model._meta.app_label == 'development' or \
            model._meta.app_label == 'expose':

            return 'admin'
        elif model._meta.app_label == 'national' :
            return 'rds'
        return 'users'

    def db_for_write(self, model, **hints):
        print('db_for_write')
        print(model._meta.app_label)
        if model._meta.app_label == 'steph_admin' or \
            model._meta.app_label == 'feeds' or\
            model._meta.app_label == 'lineup' or\
            model._meta.app_label == 'league_team_player' or \
            model._meta.app_label == 'preview_review' or \
            model._meta.app_label == 'board' or \
            model._meta.app_label == 'feedback' or \
            model._meta.app_label == 'feedback_new' or \
            model._meta.app_label == 'transfer' or \
            model._meta.app_label == 'user' or \
            model._meta.app_label == 'etc' or \
            model._meta.app_label == 'event' or \
            model._meta.app_label == 'poll' or \
            model._meta.app_label == 'info_update' or \
            model._meta.app_label == 'development' or \
            model._meta.app_label == 'expose':
            return 'admin'
        elif model._meta.app_label == 'national' :
            return 'rds'
        return 'users'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'steph_admin': return False
        else : return True
