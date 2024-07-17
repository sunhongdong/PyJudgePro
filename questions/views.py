from rest_framework.viewsets import ModelViewSet
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.decorators import action


class QuestionsView(ModelViewSet):
    # 这些就代表是最简单的写法
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    """
    detail = True  表示 操作单个对象，但不知道是不是id
    false 表示操作多个对象，
    
    """

    @action(detail=True, methods=['GET'])
    def test(self, request):
        pass

    @action(methods=['POST'], detail=False)
    def test01(self, request):
        pass




