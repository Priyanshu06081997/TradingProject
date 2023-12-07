from django.urls import path, include
from rest_framework import routers
from .views import CsvViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register('upload_csv', CsvViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]