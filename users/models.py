from django.contrib.auth.models import User
from django.db import models
from product.models import Product

'''
class Users(models.Model):
    email = models.CharField(verbose_name="이메일", max_length = 128)
    password = models.CharField(max_length = 80, verbose_name = "비밀번호" )
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    level = models.CharField(verbose_name="사용자 등급", max_length=8,
    choices = (('admin', '관리자'), ('user', '일반 사용자')))

    def __str__(self):
        return self.email

    class Meta:
        db_table = "shop_users"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'