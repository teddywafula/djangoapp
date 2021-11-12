from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField('date of birth')
    registration_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField("date of birth")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dormitory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student)


class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):

        return str(self.student) + " - " + str(self.subject)


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return self.grade


class StudentDormitory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dormitory)

