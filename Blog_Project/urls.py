from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('accounts/logout', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
