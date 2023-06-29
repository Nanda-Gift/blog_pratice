from django.urls import path
from blogapp import views

urlpatterns = [
        path('', views.home,name="home"),
        path('register',views.register,name='register'),
        path('login',views.login,name='login'),
        path('logouts',views.logouts,name='logouts'),
        path('create_blog',views.create_blog,name='create_blog'),
        path('know/<id>',views.know,name="know"),
        path('blog_update/<id>',views.blog_update,name='blog_update'),
        path('delete/<id>',views.delete,name='delete'),


        
]
