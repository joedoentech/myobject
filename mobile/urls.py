#移动端子路由
from django.urls import path
from .views import index

urlpatterns = [
    path('', index.index,name="mobile_index"),
]