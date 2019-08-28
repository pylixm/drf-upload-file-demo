# -*- coding:utf-8 -*-
from django.urls import path, re_path
from rest_framework import routers
from .views import AirticleViewSet, ImageUploadView


router = routers.DefaultRouter()
router.register('airticle', AirticleViewSet, basename='airticle')

urlpatterns = [
    re_path(r'^airticle/upload/(?P<filename>[^/]+)$', ImageUploadView.as_view())
] + router.urls