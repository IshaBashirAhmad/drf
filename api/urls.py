from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailsView),

    # path('employees/', views.EmployeeView.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view())

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>', views.BlogsDetailsView.as_view()),
    path('comments/<int:pk>', views.CommentsDetailsView.as_view()),

    path('', include(router.urls)),
]