from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.loginUser,name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/',views.register,name='register'),
    path('home/', views.pwdpage, name= "home"),
     path('add/', views.add, name='add'),
     path('add/addrecord/', views.addrecord, name='addrecord'),
     path('delete/<int:id>', views.delete, name='delete'),
     path('update/<int:id>', views.update, name='update'),
     path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]