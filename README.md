# sherlock
Modult `cx_Oracle` is requirement
## Cascade
settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'cascade': {
        'ENGINE':'django.db.backends.oracle',
        'NAME': 'super:1521/orcl',
        'USER': 'reader',
        'PASSWORD': 'reader',
   },
}

DATABASE_ROUTERS = ['cascade.routers.DBRouter']
```

./manage.py inspectdb --database=cascade
