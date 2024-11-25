from django.urls import path
from . import views

urlpatterns = [
    path('payslip/list/', views.Payslip_List.as_view()),
    path('payslip/detail/<int:pk>/', views.Payslip_Detail.as_view()),
]
