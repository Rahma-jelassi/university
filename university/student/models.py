from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Subject(models.Model):
    libelle = models.CharField(max_length=20)
    def __str__(self):
        return self.libelle

class Classes(models.Model):
    libelle = models.CharField(max_length=20)
    matiere = models.ManyToManyField(Subject)
    def __str__(self):
        return self.libelle 

class Student(models.Model):
    student_profile = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete= models.CASCADE,related_name='+')
    student_classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
    def __str__(self):
        return self.student_profile.username

class Student_Subject (models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    note_ds = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    note_ex = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    def moy(self):
        return self.note_ds * 0.4 + self.note_ex * 0.6
    def __str__(self):
        return f'{self.student} -> {self.subject}'
    
class Teacher(models.Model):
    profile = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete= models.CASCADE,related_name='+')
    teacher_subject=models.ManyToManyField(Subject)

    def __str__(self):
        return self.profile.username

