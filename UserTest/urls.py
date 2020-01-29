from django.urls import path

from UserTest import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.Login, name='login'),
    path('logout_user/',views.Logout,name='logout_user'),
    path('upload/',views.uploadFile,name='upload'),
]