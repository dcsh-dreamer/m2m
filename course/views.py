from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Course, Student
from .forms import CourseAddMemberForm
from django import forms
import csv

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

class CourseAddMember(FormView):
    form_class = CourseAddMemberForm
    template_name = 'form.html'

    def form_valid(self, form):
        data = form.cleaned_data['data']
        for line in data.split('\r\n'):
            fields = line.split(',')
            stu_list = Student.objects.filter(sno=fields[0])
            if stu_list:
                stu = stu_list[0]
                stu.name = fields[1]
            else:
                stu = Student(
                    sno = fields[0],
                    name = fields[1]
                )
            stu.save()
            stu.course.add(self.kwargs['cid'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('course_view', args=[self.kwargs['cid']])

class StudentEdit(UpdateView):
    model = Student
    pk_url_kwarg = 'sid'
    template_name = 'form.html'
    fields = '__all__'

    def get_form(self):
        form = super().get_form()
        widget = form.fields['course'].widget
        form.fields['course'].widget = forms.CheckboxSelectMultiple(choices = widget.choices)
        return form

    def get_success_url(self):
        return reverse('course_view', args=[self.object.course.all()[0].id])