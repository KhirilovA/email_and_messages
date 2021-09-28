from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from api import views

router = DefaultRouter()

router.register('create', views.MessageViewSet, basename='create')
router.register('list', views.MessageListViewSet, basename='list')
router.register('single', views.SingleMessageViewSet, basename='single')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/messages/', include(router.urls)),
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title='MessageApi',
        description='Api for the MessageApi',
        version='1.0.0'
        ), name='openapi-schema')
]