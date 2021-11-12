from django.shortcuts import render

from .models import Tutor, Subject, Student, Grade, Dormitory
from django.http import HttpResponse

from django.http import Http404
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = "students.html"
    context_object_name = "items"

    def get_queryset(self):
        return Student.objects.all()


class DetailView(generic.DetailView):
    model = Student
    template_name = "student_details.html"


class DormitoryView(generic.ListView):
    template_name = "dormitory.html"
    context_object_name = "items"

    def get_queryset(self):
        return Dormitory.objects.all()


class DormitoryDetailView(generic.DetailView):
    model = Dormitory
    template_name = "dormitory_details.html"


def hello(request):
    return render(request, "hello.html")


def grades(request):
    return HttpResponse("grades")


def dormitory(request):
    return HttpResponse("dormitory")


def tutor(request):
    return HttpResponse("tutor")


def subject(request):
    return HttpResponse("subject")
