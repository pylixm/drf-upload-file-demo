from django.db import models

# Create your models here.


class Airticle(models.Model):
    title = models.CharField('标题', max_length=200)
    image = models.ImageField('题图', upload_to='airticle/')
    content = models.TextField('正文')
    create_at = models.DateTimeField('创建时间', blank=True, auto_now_add=True)
    update_at = models.DateTimeField('更新时间', blank=True, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
