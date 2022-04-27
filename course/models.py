from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField('課程/班級名稱', max_length=128)
    ctype = models.IntegerField('類型', choices = [
        (0, '課程'), 
        (1, '班級'),
    ])

    def __str__(self):
        return self.name

class Student(models.Model):
    sno = models.CharField('學號', max_length=16)
    name = models.CharField('姓名', max_length=16)
    course = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name