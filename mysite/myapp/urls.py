from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('tutor', views.tutor, name='tutor'),
    # path('student', views.student, name='student'),
    path('student', views.IndexView.as_view(), name='student'),
    path('grades', views.grades, name='grades'),
    path('dormitory', views.dormitory, name='dormitory'),
    path('subject', views.subject, name='subject'),
    path('<int:student_id>/student', views.student_details, name='student_details')
]