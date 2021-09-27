from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('post/create', MessageViewSet)
app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]