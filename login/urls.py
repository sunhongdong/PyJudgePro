from rest_framework.routers import DefaultRouter
from .views import RegisterViews, LoginViews, LogoutViews

router = DefaultRouter()
router.register(r'', RegisterViews)
router.register(r'', LoginViews)
router.register(r'', LogoutViews)

urlpatterns = router.urls
