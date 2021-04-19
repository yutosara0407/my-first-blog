from django.db import models
from django.utils import timezone

class Circle(models.Model):
    name = models.CharField('サークル', max_length=20)
    
    def __str__(self):
        return self.name

class Gymnasium(models.Model):
    name = models.CharField('体育館', max_length=20)
    address = models.CharField('体育館住所', max_length=80)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField('氏名', max_length=20)
    nickname = models.CharField('ニックネーム', max_length=20)
    email = models.EmailField('メールアドレス',blank=True)
    circle = models.ManyToManyField(
        Circle, verbose_name='サークル',
    )
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return'{0}{1}{2}'.format(self.name, self.nickname, self.circle)