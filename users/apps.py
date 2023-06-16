from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

'''
#signals.py와 같이 삭제
    def ready(self):
        import users.signals
'''