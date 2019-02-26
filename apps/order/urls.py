from  django.conf.urls import url

from apps.user import views
urlpatterns = [
    url(r'^$', views.index),  # 用户模块

]
