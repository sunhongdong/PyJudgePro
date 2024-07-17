from rest_framework import serializers
from .models import Question


# 自动 生成序列化的数据

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        # data = serializers.DateTimeField(source='') # 改名称
        model = Question

        fields = '__all__'  # 和exclude 只能存在一个

        # exclude=[''] # 去除哪个的操作
