from django.conf.urls import url

from apps.user import views
from apps.user.views import RegisterView

urlpatterns = [
    url(r'^$', views.index),  # 用户模块
    # url(r'^register$', views.register),  # 注册模块
    # url(r'^register_handle$', views.register_handle),
    url(r'^register$', RegisterView.as_view(), name='register'),
]
