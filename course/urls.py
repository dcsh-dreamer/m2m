from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseList.as_view(), name='course_list'),
    path('<int:cid>/', CourseView.as_view(), name='course_view'),
    path('create/', CourseCreate.as_view(), name='course_create'),
]
