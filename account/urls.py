from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.UserLoginView.as_view(), name='user_login'),
    url(r'logout/$', views.UserLogoutView.as_view(), name='user_logout'),
]
