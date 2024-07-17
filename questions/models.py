from django.db import models
from django.utils import timezone
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=512, null=True, blank=True, verbose_name='标题')
    content = models.TextField(null=True, blank=True, verbose_name='内容')
    tags = models.JSONField(null=True, blank=True, verbose_name='标签列表')
    answer = models.TextField(null=True, blank=True, verbose_name='题目答案')
    submitNum = models.IntegerField(default=0, verbose_name='题目提交数')
    acceptedNum = models.IntegerField(default=0, verbose_name='题目通过数')
    judgeCase = models.JSONField(null=True, blank=True, verbose_name='判题用例')
    judgeConfig = models.JSONField(null=True, blank=True, verbose_name='判题配置')
    thumbNum = models.IntegerField(default=0, verbose_name='点赞数')
    favourNum = models.IntegerField(default=0, verbose_name='收藏数')
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    createTime = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'question'
        verbose_name = '题目'
        verbose_name_plural = '题目'
        ordering = ['-thumbNum']
        indexes = [
            models.Index(fields=['userId'], name='idx_userId'),
        ]

    def __str__(self):
        return self.title or f"Question {self.id}"
