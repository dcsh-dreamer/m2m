from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course, Student

# Create your views here.
class CourseList(ListView):
    model = Course

class CourseView(DetailView):
    model = Course
    pk_url_kwarg = 'cid'

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('course_view', args=[self.object.id])