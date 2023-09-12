from django.db import models

# Create your models here.
class Board(models.Model):
    category = models.CharField(max_length=100)
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