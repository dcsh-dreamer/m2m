from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseList.as_view(), name='course_list'),
    path('course/<int:cid>/', CourseView.as_view(), name='course_view'),
    path('course/create/', CourseCreate.as_view(), name='course_create'),
]
