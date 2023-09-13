from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#사용자
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(verbose_name="아이디", max_length=50)
    user_pwd = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=100,unique=True)
    user_login_date = models.DateTimeField(auto_now_add=True) #사용자가 로그인한 날짜와 시간을 저장

class Category(models.Model):
    category_name = models.CharField(max_length=30)


class Board(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    # upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=200, default = '')

    # 게시글 임시 관련 데이터베이스 모델 정의 (임시저장 기능 포함)
    title =models.CharField(max_length=100)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)  # 게시글이 임시 저장인지 여부를 나타내는 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



