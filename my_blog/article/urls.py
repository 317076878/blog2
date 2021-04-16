from django.urls import path
from .views import *

urlpatterns = [
    path('article-list/', article_list, name='article_list'),
    # 文章详情
    path('article-detail/<int:id>/', article_detail, name='article_detail'),
    path('article-create/', article_create, name='article_create'),
    path('article-safe-delete/<int:id>/', article_safe_delete, name='article_safe_delete'),
    path('article-update/<int:id>/', article_update, name='article_update'),
]