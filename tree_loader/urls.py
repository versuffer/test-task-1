from django.urls import path

from .views import EmployeeTreeView

urlpatterns = [
    path('', EmployeeTreeView)
]
