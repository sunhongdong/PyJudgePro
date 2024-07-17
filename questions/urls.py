from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionsView

router = DefaultRouter()
router.register(r'', QuestionsView)

urlpatterns = router.urls
