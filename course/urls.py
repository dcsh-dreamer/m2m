from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseList.as_view(), name='course_list'),
    path('course/<int:cid>/', CourseView.as_view(), name='course_view'),
    path('course/create/', CourseCreate.as_view(), name='course_create'),
    path('course/<int:cid>/add/', CourseAddMember.as_view(), name='course_add_member'),
    path('student/<int:sid>/', StudentEdit.as_view(), name='student_edit'),
]
