from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
  # path('', include('django.contrib.auth.urls')),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register')
]