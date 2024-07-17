from django.db import models
from django.conf import settings


class QuestionSubmit(models.Model):
    # 判题状态选项
    class JudgeStatus(models.IntegerChoices):
        WAITING = 0, '待判题'
        JUDGING = 1, '判题中'
        ACCEPTED = 2, '成功'
        FAILED = 3, '失败'

    # 判题结果选项
    class JudgeResult(models.TextChoices):
        ACCEPTED = 'AC', 'Accepted'
        WRONG_ANSWER = 'WA', 'Wrong Answer'
        COMPILE_ERROR = 'CE', 'Compile Error'
        MEMORY_LIMIT_EXCEEDED = 'MLE', 'Memory Limit Exceeded'
        TIME_LIMIT_EXCEEDED = 'TLE', 'Time Limit Exceeded'
        PRESENTATION_ERROR = 'PE', 'Presentation Error'
        OUTPUT_LIMIT_EXCEEDED = 'OLE', 'Output Limit Exceeded'
        WAITING = 'WT', 'Waiting'
        DANGEROUS_OPERATION = 'DO', 'Dangerous Operation'
        RUNTIME_ERROR = 'RE', 'Runtime Error'
        SYSTEM_ERROR = 'SE', 'System Error'

    language = models.CharField(max_length=128, verbose_name='编程语言')
    code = models.TextField(verbose_name='用户代码')

    # 替换 JSONField，使用具体的字段
    status = models.IntegerField(
        choices=JudgeStatus.choices,
        default=JudgeStatus.WAITING,
        verbose_name='判题状态'
    )
    judgeResult = models.CharField(
        max_length=3,
        choices=JudgeResult.choices,
        default=JudgeResult.WAITING,
        verbose_name='判题结果'
    )
    executionTime = models.FloatField(null=True, blank=True, verbose_name='执行时间(ms)')
    memoryUsage = models.IntegerField(null=True, blank=True, verbose_name='内存使用(KB)')
    errorMessage = models.TextField(null=True, blank=True, verbose_name='错误信息')

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE, verbose_name='题目')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='创建用户')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        indexes = [
            models.Index(fields=['question']),
            models.Index(fields=['user']),
        ]
        verbose_name = '题目提交'
        verbose_name_plural = '题目提交'

    def __str__(self):
        return f"Submission {self.id} by {self.user.username} for Question {self.question.id}"
