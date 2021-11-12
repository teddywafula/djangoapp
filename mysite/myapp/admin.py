from django.contrib import admin

# Register your models here.
from .models import Student, Grade, Subject, Dormitory,StudentDormitory,StudentClass,Marks,StudentSubject, Tutor

admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Dormitory)
admin.site.register(StudentDormitory)
admin.site.register(StudentClass)
admin.site.register(StudentSubject)
admin.site.register(Marks)
admin.site.register(Tutor)
