from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailsView),

    path('employees/', views.EmployeeView.as_view() )
]