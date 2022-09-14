from .views import TheNewsViewSet, TypeNewsViewSet
from rest_framework.routers import DefaultRouter
from typing import List

router = DefaultRouter()
router.register(r'news', TheNewsViewSet, basename='news')
router.register(r'types', TypeNewsViewSet, basename='types')

urlpatterns: List = router.urls
