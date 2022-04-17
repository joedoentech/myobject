#后台管理子路由
from django.contrib import admin
from django.urls import path,include
from myadmin.views import index

urlpatterns = [
    path('', include('web.urls')),
    path('myadmin/', include('myadmin.urls')),
    path('mobile/', include('mobile.urls')),
]