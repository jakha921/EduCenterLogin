from django.urls import path, include
from . import views

#! TODO:
# ?*  regions
# ?*  schools
# ?*  courses
# ?*  groups
# ?*  teachers
# ?*  clients
# ?*  parents
# ?  tests
# ?*  lessons
# ?*  attentions

urlpatterns = [
    # path('', views.index, name='index'),
    path('sign', views.sign, name='sign'),
    path('create_user', views.create_user, name='create_user'),
    path('create_parent', views.create_parent, name='create_parent'),
    path('regions', views.regionsCreateAPIView.as_view(), name='regions'),
    path('regionsUpd/<int:pk>/', views.regionsUpdAPIView.as_view()),
    path('schools', views.schoolsCreateAPIView.as_view(), name='schools'),
    path('schoolsUpd/<int:pk>/', views.schoolsUpdAPIView.as_view()),
    path('courses', views.coursesCreateAPIView.as_view(), name='courses'),
    path('coursesUpd/<int:pk>/', views.coursesUpdAPIView.as_view()),
    path('groups', views.groupsCreateAPIView.as_view(), name='groups'),
    path('groupsUpd/<int:pk>/', views.groupsUpdAPIView.as_view()),
    path('teachers', views.teachersCreateAPIView.as_view(), name='teachers'),
    path('teachersUpd/<int:pk>/', views.teachersUpdAPIView.as_view()),
    path('clients', views.clientsCreateAPIView.as_view(), name='clients'),
    path('clientsUpd/<int:pk>/', views.clientsUpdAPIView.as_view()),
    path('parents', views.parentsCreateAPIView.as_view(), name='clients'),
    path('parentsUpd/<int:pk>/', views.parentsUpdAPIView.as_view()),
    path('lessons', views.lessonsCreateAPIView.as_view(), name='lessons'),
    path('lessonsUpd/<int:pk>/', views.lessonsUpdAPIView.as_view()),
    path('attentions', views.attentionsCreateAPIView.as_view(), name='attentions'),
    path('attentionsUpd/<int:pk>/', views.attentionsUpdAPIView.as_view()),
    # path('test', views.teachersCreateAPIView.as_view(), name='test'),
    path('auth', include('rest_framework.urls'), name='auth'),
]
