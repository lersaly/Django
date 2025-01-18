from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('topic/<int:topic_id>/rate/', views.topic_rate, name='topic_rate'),
    path('course/<int:pk>/enroll/', views.course_enroll, name='course_enroll'),
    path('course/<int:course_id>/topic/add/', views.topic_create, name='topic_create'),
    path('course/<int:pk>/unenroll/', views.course_unenroll, name='course_unenroll'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
    
]