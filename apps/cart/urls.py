from  django.conf.urls import url

from apps.cart import views
urlpatterns = [
    url(r'^$', views.index),  # 用户模块

]
