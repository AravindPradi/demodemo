from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('admin',views.admin,name='admin'),
    path('addcourse',views.addcourse,name='c_add'),
    path('register_fn',views.register_fn,name='register_fn'),
    path('teacherpage',views.teacherpage,name='teacherpage'),
    path('update_teacher/<int:pk>',views.update_teacher,name='update'),
]