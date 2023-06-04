from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    # main
    path('',views.home,name='home'),
    path('upload/',views.upload,name='upload'),

    # auth
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',LogoutView.as_view(),name='logout')
    
]