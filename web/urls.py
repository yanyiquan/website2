"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from web import views, settings
from django.views.static import serve
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('index/', views.index),
    path('slr/', views.slr, name='slr'),
    path('tolerance/', views.baseline),
    path('invtype/', views.invtype),
    path('esg/', views.esg),
    path('trends/', views.trends),
    path('admin/', admin.site.urls),
    path('login/', views.clientLogin, name='clientLogin'),
    path('logout/', views.clientLogout, name='clientLogout'),
    path('submitTolerance/', views.submitTolerance, name='submitTolerance'),
    path('submitInvtype/', views.submitInvtype, name='submitInvtype'),
    path('submitESG/', views.submitESG, name='submitESG'),
    path('submitSLR/', views.submitSLR, name='submitSLR'),
    path('submitTrends/', views.submitTrends, name='submitTrends'),
    path('result/', views.result, name='result'),
    path('downloadreport/', views.dlreport),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path(r'favicon.ico', RedirectView.as_view(url=r'/static/images/favicon.ico')),
]

