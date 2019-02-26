"""daylifresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^',include())

    url(r'^tinymce/', include('tinymce.urls')),  # 用户模块

    url(r'^users/', include(('apps.user.urls', 'users'), namespace='users')),
    url('cart/', include(('apps.cart.urls', 'apps'), namespace='cart')),
    url('order/', include(('apps.order.urls', 'apps'), namespace='order')),
    url('^goods/', include(('apps.goods.urls', 'apps'), namespace='goods')),
    # url('', include(('apps.user.urls', 'apps'), namespace='apps-user')),
    # url('', include(('apps.cart.urls', 'apps'), namespace='apps-cart')),
    # url('', include(('apps.order.urls', 'apps'), namespace='apps-order')),
    # url('', include(('apps.goods.urls', 'apps'), namespace='apps-goods')),

    # url(r'^user/', include('apps.user.urls')),
    # url(r'^cart/', include('apps.cart.urls')),
    # url(r'^order/', include('apps.order.urls')),
    # url(r'^', include('apps.goods.urls')),

]
