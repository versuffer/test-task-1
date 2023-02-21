from django.urls import path

from .views import employee_tree_view

urlpatterns = [
    path('', employee_tree_view)
]
