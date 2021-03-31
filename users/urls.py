from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [ #登录页面
				path('login/', LoginView.as_view(template_name='users/login.html'), name = 'login'),
				#注销账号
				path('logout/', views.logout_view, name='logout'),
				#注册页面
				path('register/', views.register, name='register'),
]
