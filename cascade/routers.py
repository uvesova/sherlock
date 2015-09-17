# import logging
# logger = logging.getLogger(__name__)

django_apps = [
   'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles'
]

class DBRouter(object):
    def db_for_read(self, model, **hints):
        label = model._meta.app_label
        # logger.error('='*60+'read')
        # logger.error("Label:" + label)
        # logger.error("model._meta.db_table:"+model._meta.db_table)
        if label not in django_apps:
            dbName = 'cascade'
        else:
            dbName = 'default'
        # logger.error('='*20 + ' app:'+label+' db:' + dbName + '='*20)
        return dbName

    def db_for_write(self, model, **hints):
        label = model._meta.app_label
        # logger.error(label + '='*40+'write')
        if label not in django_apps:
            return 'cascade'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        # label1 = obj1._stat.db
        # label2 = obj2._stat.db
        if label1 == label2:
            return True
        return False

    def allow_migrate(self, db, model):
        label = model._meta.app_label
        if label.startswith('dj'):
            return True
        return False
