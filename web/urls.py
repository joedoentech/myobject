#前台大堂点餐端子路由
from django.urls import path
from .views import index

urlpatterns = [
    path('', index.index,name="myadmin_index"),
]