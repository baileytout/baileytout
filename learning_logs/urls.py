"""定义learning_logs的URL模式"""
from django.urls import path
from . import views
urlpatterns = [ #主页
				path('', views.index, name = 'index'),
				#显示所有主题的页面
				path('topics/', views.topics, name = 'topics'),
				path('topics/<topic_id>/', views.topic, name = 'topic'),
				path('new_topic/', views.new_topic, name = 'new_topic'),
				path('new_entry/<topic_id>', views.new_entry, name = 'new_entry'),
				path('edit_entry/<entry_id>', views.edit_entry, name = 'edit_entry'),
]
